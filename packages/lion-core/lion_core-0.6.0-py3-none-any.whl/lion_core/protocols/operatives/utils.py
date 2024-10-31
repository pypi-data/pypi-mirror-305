import inspect

from lionfuncs import copy, validate_boolean
from pydantic import (
    BaseModel,
    Field,
    PrivateAttr,
    create_model,
    field_validator,
    model_validator,
)
from pydantic.fields import FieldInfo
from typing_extensions import Self

from lion_core.protocols.fields.action_responses_ import ACTION_RESPONSES_FIELD
from lion_core.protocols.models import FieldModel, ParamsModel


class PrepFieldParamsModel(ParamsModel):

    parameters: dict[str, FieldInfo] = Field(default_factory=dict)
    base: type[BaseModel] = Field(default=BaseModel)
    exclude_fields: list = Field(default_factory=list)
    include_fields: list = Field(default_factory=list)
    field_descriptions: dict = Field(default_factory=dict)
    use_base_kwargs: bool = Field(default=False)
    use_all_fields: bool = Field(default=False)
    name: str = Field(default="StepModel")
    class_kwargs: dict = Field(default_factory=dict)
    field_models: list[FieldModel] = Field(default_factory=list)
    request_model_type: type[BaseModel] | None = Field(default=None)
    response_model_type: type[BaseModel] | None = Field(default=None)
    request_model: BaseModel | None = Field(default=None)
    response_model: BaseModel | None = Field(default=None)
    inherit_base: bool = Field(default=True)
    str_dict_response: str | dict | None = None
    use_fields: dict[str, tuple] | None = None

    _validators: dict[str, callable] | None = PrivateAttr(default=None)

    @field_validator("parameters", mode="before")
    def validate_parameters(cls, value):
        if value is None:
            return {}
        if not isinstance(value, dict):
            raise ValueError("Fields must be a dictionary.")
        for k, v in value.items():
            if not isinstance(k, str):
                raise ValueError("Field names must be strings.")
            if not isinstance(v, FieldInfo):
                raise ValueError("Field values must be FieldInfo objects.")
        return copy(value)

    @field_validator("base", mode="before")
    def validate_base(cls, value):
        if value is None:
            return BaseModel
        if isinstance(value, type) and issubclass(value, BaseModel):
            return value
        if isinstance(value, BaseModel):
            return value.__class__
        raise ValueError("Base must be a BaseModel subclass or instance.")

    @field_validator("exclude_fields", "include_fields", mode="before")
    def validate_fields(cls, value):
        if value is None:
            return []
        if isinstance(value, dict):
            value = list(value.keys())
        if isinstance(value, list):
            value = list(value)
        if isinstance(value, list):
            if not all(isinstance(i, str) for i in value):
                raise ValueError("Field names must be strings.")
            return copy(value)
        raise ValueError("Fields must be a list, set, or dictionary.")

    @field_validator("field_descriptions", mode="before")
    def validate_field_descriptions(cls, value):
        if value is None:
            return {}
        if not isinstance(value, dict):
            raise ValueError("Field descriptions must be a dictionary.")
        for k, v in value.items():
            if not isinstance(k, str):
                raise ValueError("Field names must be strings.")
            if not isinstance(v, str):
                raise ValueError("Field descriptions must be strings.")
        return value

    @field_validator("use_base_kwargs", "use_all_fields", mode="before")
    def validate_use_base_kwargs(cls, value):
        try:
            return validate_boolean(value)
        except Exception as e:
            raise ValueError(
                f"Failed to convert {value} to a boolean. Error: {e}"
            ) from e

    @field_validator("name", mode="before")
    def validate_name(cls, value):
        if value is None:
            return "StepModel"
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        return value

    @field_validator("class_kwargs", mode="before")
    def validate_class_kwargs(cls, value):
        if value is None:
            return {}
        if not isinstance(value, dict):
            raise ValueError("Class kwargs must be a dictionary.")
        for k, v in value.items():
            if not isinstance(k, str):
                raise ValueError("Class keyword names must be strings.")
        return value

    @field_validator("field_models", mode="before")
    def validate_field_models(cls, value):
        if value is None:
            return []
        value = [value] if not isinstance(value, list) else value
        if not all(isinstance(i, FieldModel) for i in value):
            raise ValueError("Field models must be FieldModel objects.")
        return value

    @model_validator(mode="after")
    def validate_param_model(self) -> Self:
        if any([i in self.exclude_fields for i in self.include_fields]):
            raise ValueError(
                "Operation include fields and exclude fields cannot"
                " have common elements."
            )
        if self.field_models:
            self.parameters.update(
                {f.name: f.field_info for f in self.field_models}
            )

        if self.base:
            if self.use_all_fields and hasattr(self.base, "all_fields"):
                self.parameters.update(copy(self.base.all_fields))
            elif hasattr(self.base, "model_fields"):
                self.parameters.update(copy(self.base.model_fields))

        use_keys = list(self.parameters.keys())

        if self.exclude_fields:
            use_keys = [i for i in use_keys if i not in self.exclude_fields]

        self.parameters = {
            k: v for k, v in self.parameters.items() if k in use_keys
        }

        validators = {}
        for i in self.field_models:
            if i.field_validator is not None:
                validators.update(i.field_validator)
        self._validators = validators

        if self.field_descriptions:
            for field_name, description in self.field_descriptions.items():
                if description and field_name in self.parameters:
                    self.parameters[field_name] = self.parameters[
                        field_name
                    ].model_copy(update={"description": description})

        # Prepare class attributes
        class_kwargs = {}
        if self.use_base_kwargs:
            class_kwargs.update(
                {
                    k: getattr(self.base, k)
                    for k in self.base.__dict__
                    if not k.startswith("__")
                }
            )

        if hasattr(self.base, "class_name"):
            if callable(self.base.class_name):
                self.name = self.base.class_name()
            else:
                self.name = self.base.class_name
        elif inspect.isclass(self.base):
            self.name = self.base.__name__

            self.use_fields = {
                k: (v.annotation, v) for k, v in self.parameters.items()
            }
        return self

    @classmethod
    def as_request_model_type(cls, **kwargs) -> "PrepFieldParamsModel":
        self = cls.model_validate(kwargs)

        if not self.request_model_type:
            self.request_model_type = create_model(
                self.name + "Request",
                __config__=kwargs.pop("config_dict", None),
                __doc__=kwargs.pop("doc", None),
                __base__=self.base if self.inherit_base else BaseModel,
                __validators__=self._validators,
                __cls_kwargs__=self.class_kwargs,
                **self.use_fields,
            )
            if kwargs.pop("frozen", False) is True:
                self.request_model_type.model_config.frozen = True
        return self

    @classmethod
    def as_response_model_type(
        cls,
        request_params: "PrepFieldParamsModel",
        field_models: list[FieldModel] = None,
        **kwargs,
    ) -> "PrepFieldParamsModel":
        if (
            request_params.request_model is None
            or request_params.str_dict_response is None
        ):
            raise ValueError(
                "A completed Step Request model must be provided,"
                " you cannot generate a response model without a "
                "request model."
            )
        params = request_params.request_model_type.model_fields
        field_models = field_models or []
        field_models.extend(request_params.field_models)

        self = cls(
            parameters=params,
            base=request_params.base,
            exclude_fields=request_params.exclude_fields,
            use_base_kwargs=request_params.use_base_kwargs,
            name=request_params.name,
            inherit_base=request_params.inherit_base,
            field_descriptions=request_params.field_descriptions,
            use_all_fields=request_params.use_all_fields,
            field_models=field_models,
            validators={
                **(kwargs.pop("response_validators", None) or {}),
                **(request_params._validators or {}),
            },
        )

        self.response_model_type = create_model(
            self.name + "Response",
            __config__=kwargs.pop("response_config_dict", None),
            __doc__=kwargs.pop("response_doc", None),
            __base__=self.base if self.inherit_base else BaseModel,
            __validators__=self._validators,
            __cls_kwargs__=self.class_kwargs,
            **self.use_fields,
        )
        if kwargs.pop("frozen", False) is True:
            self.request_model_type.model_config.frozen = True

        return self

    @classmethod
    def parse_request_to_response_model(
        cls,
        request_params: "PrepFieldParamsModel",
        response_validators: dict = None,
        frozen_reponse: bool = False,
        response_config_dict=None,
        response_doc=None,
        action_responses: list = None,
        **kwargs,
    ) -> dict:

        if (
            action_responses
            and ACTION_RESPONSES_FIELD not in request_params.field_models
        ):
            request_params.field_models.append(ACTION_RESPONSES_FIELD)

        response_param = cls.as_response_model_type(
            request_params=request_params,
            response_validators=response_validators,
            frozen_reponse=frozen_reponse,
            response_config_dict=response_config_dict,
            response_doc=response_doc,
        )

        if request_params.request_model:
            kwargs.update(request_params.request_model.model_dump())
        elif isinstance(request_params.str_dict_response, dict):
            kwargs.update(request_params.str_dict_response)

        return response_param.response_model_type.model_validate(kwargs)
