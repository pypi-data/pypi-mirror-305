import typing
from typing import Optional, Union, Iterable
import sys
import importlib
import functools
import re

import attrs
from attrs import define, field

import pydantic
from pydantic import BaseModel, ConfigDict
from pyspark.sql import DataFrame, types as T, functions as F

from .transform import cdm_transform
from .validate import cdm_validate


class CommonDataModel(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    @classmethod
    def get_columns(cls, pattern: str = None, dtype: T.DataType = None) -> list[str]:
        """Obtain columns by parameters. By default, all columns are returned."""
        if pattern:
            pattern = re.compile(pattern)
            return [field for field in cls.model_fields if pattern.search(field)]
        if dtype:
            return [
                field
                for field, field_info in cls.model_fields.items()
                if isinstance(field_info.annotation, dtype)
            ]
        return list(cls.model_fields.keys())

    @classmethod
    def get_schema(cls):
        return T.StructType(
            [
                T.StructField(field_name, T.StringType())
                for field_name in cls.model_fields.keys()
            ]
        )

    @classmethod
    def get_required_fields(cls):
        return [
            field
            for field, annotation in typing.get_type_hints(cls).items()
            if not typing.get_origin(annotation) is Union
        ]

    @classmethod
    def _read(
        cls,
        func: callable = None,
        module: str = "cortexpy.context.entry_context",
        submodule: str = "get_context",
        *args: tuple,
        **kwargs: dict,
    ) -> callable:
        if module.split(".")[0] in sys.modules:
            loaded_module = getattr(importlib.import_module(module), submodule)
            func = getattr(loaded_module(), "read")
        return functools.partial(func, schema=cls.get_schema(), *args, **kwargs)

    @classmethod
    def _write(cls, func: callable = None, **kwargs: dict) -> callable:
        if "cortexpy" in sys.modules:
            cortexpy_module = getattr(
                importlib.import_module("cortexpy.context.entry_context"), "get_context"
            )
            func = getattr(cortexpy_module(), "write")
        return functools.partial(func, schema=cls.get_schema(), **kwargs)

    @classmethod
    def format_options(
        cls, source: list[str], read_options: dict[str, Iterable]
    ) -> list[dict]:
        """Distribute, format reading options as list of keyword arguments."""
        options_length = (
            len(option)
            for option in read_options.values()
            if isinstance(option, (list, tuple))
        )
        max_options_length = max([1, *options_length])
        read_options = [
            {
                "source": file,
                **{
                    key: option[i] if isinstance(option, (list, tuple)) else option
                    for key, option in read_options.items()
                },
            }
            for file in source
            for i in range(max_options_length)
        ]
        return read_options

    @classmethod
    def read(
        cls,
        source: list[str],
        preprocessing: Optional[callable] = None,
        read_options: Optional[dict] = None,
    ) -> DataFrame:
        """Load, transform, validate all soures passed to the model with optional preprocessing function"""

        @cdm_validate(model=cls)
        @cdm_transform(model=cls)
        def etl_chain(etl_kwargs: list[dict]) -> DataFrame:
            """Generic read-in function for loading, transforming, and validating data"""
            data = functools.reduce(
                DataFrame.unionByName,
                map(lambda kw: cls._read(**kw)(kw.get("source")), etl_kwargs),
            )
            data = preprocessing(data) if preprocessing else data
            return data

        if read_options:
            etl_kwargs = cls.format_options(source=source, read_options=read_options)
        else:
            etl_kwargs = {"source": source}
        return etl_chain(etl_kwargs)


@define(slots=False)
class CommonAnalytic:
    name: str = field(default="...")
    description: str = field(default="...")

    @classmethod
    def get_analytic_models(cls):
        """Filter class attributes for analytic-defined models"""
        from pydantic._internal._model_construction import ModelMetaclass

        return [
            field.name
            for field in attrs.fields(cls)
            if isinstance(field.type, ModelMetaclass)
        ]

    def run(self) -> None:
        """Run all analytic-specific methods"""
        import inspect

        IGNORE = ("get_analytic_models", "run", "materialize")
        analytic_methods = [
            func
            for func in inspect.getmembers(self, inspect.ismethod)
            if not (func[0].startswith("__") or func[0] in IGNORE)
        ]
        assert len(analytic_methods) > 0, "No analytic methods defined"

        num_methods = len(analytic_methods)
        method_outputs = dict()
        for i, (method_name, method) in enumerate(analytic_methods):
            print(f"[{i+1}/{num_methods}] Running `{method_name}` ...")
            method_outputs[method_name] = method()

        return method_outputs

    def materialize(
        self, source: dict
    ) -> None:  # use self to reference instance of the class
        """Update model parameters with materialized DataFrame"""
        for model in self.get_analytic_models():
            setattr(self, model, source.get(getattr(self, model)))


@define(slots=False)
class CommonPipeline:
    analytic: CommonAnalytic
    models: dict[CommonDataModel, dict]
    data: dict[CommonDataModel, dict]

    def etl_chain(
        self, data: DataFrame, model: CommonDataModel, preprocessing: callable = None
    ) -> DataFrame:
        """Process, transform, and validate a DataFrame given the passed model"""

        @cdm_validate(model=model)
        @cdm_transform(model=model)
        def process(data: DataFrame) -> DataFrame:
            if preprocessing:
                data = preprocessing(data)
            return data

        return process(data=data)

    def materialize(self) -> "CommonPipeline":
        """Perform procedures for pipeline"""
        self.data = {
            model: model.read(**parameters) for model, parameters in self.data.items()
        }
        self.models = {
            model: self.etl_chain(
                data=self.data.get(parameters.get("source")),
                model=model,
                preprocessing=parameters.get("preprocessing"),
            )
            for model, parameters in self.models.items()
        }
        self.analytic.materialize(source=self.models)
        self.outputs = self.analytic.run()
        return self
