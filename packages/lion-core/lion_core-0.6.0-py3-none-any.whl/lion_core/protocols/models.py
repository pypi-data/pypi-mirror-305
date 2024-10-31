from collections.abc import Callable
from typing import Any, TypeVar

from lionabc.exceptions import LionValueError
from lionfuncs import unique_hash
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    PrivateAttr,
    field_serializer,
    field_validator,
)
from pydantic.fields import FieldInfo
from pydantic_core import PydanticUndefined

from lion_core.types import LN_UNDEFINED

FIELD_NAME = TypeVar("FIELD_NAME", bound=str)


def clean_dump(obj: BaseModel) -> dict:
    dict_ = obj.model_dump()
    for i in list(dict_.keys()):
        if dict_[i] is LN_UNDEFINED:
            dict_.pop(i)
    return dict_


class ParamsModel(BaseModel):

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
        arbitrary_types_allowed=True,
        validate_default=False,
    )

    @classmethod
    def check_params(cls, **kwargs) -> dict:
        try:
            a = cls.model_validate(kwargs)
            return a.model_dump()
        except Exception as e:
            raise ValueError("Failed to validate parameters") from e


class SchemaModel(BaseModel):

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        extra="forbid",
        use_enum_values=True,
        populate_by_name=True,
        validate_default=True,
    )

    def to_dict(self) -> dict[str, Any]:
        return clean_dump(self)

    @classmethod
    def schema_keys(cls) -> set:
        return set(cls.model_fields.keys())


class FieldModel(BaseModel):

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        extra="allow",
        use_enum_values=True,
        populate_by_name=True,
    )

    _unique_hash: str = PrivateAttr(lambda: unique_hash(32))

    name: str = Field(..., exclude=True)
    annotation: type | Any = Field(LN_UNDEFINED, exclude=True)
    default: Any = LN_UNDEFINED
    default_factory: Any = LN_UNDEFINED
    title: str | Any = LN_UNDEFINED
    description: str | Any = LN_UNDEFINED
    examples: list | Any = LN_UNDEFINED
    validators: list | Any = LN_UNDEFINED
    exclude: bool | Any = LN_UNDEFINED
    validator: Callable | Any = Field(LN_UNDEFINED, exclude=True)
    validator_kwargs: dict | Any = Field(default_factory=dict, exclude=True)

    def to_dict(self) -> dict[str, Any]:
        return clean_dump(self)

    @property
    def field_info(self) -> FieldInfo:
        annotation = (
            self.annotation if self.annotation is not LN_UNDEFINED else Any
        )
        field_obj = Field(**self.to_dict())  # type: ignore
        field_obj.annotation = annotation
        return field_obj

    @property
    def field_validator(self) -> dict[str, Callable]:
        if self.validator is LN_UNDEFINED:
            return None
        kwargs = self.validator_kwargs or {}
        return {
            f"{self.name}_validator": field_validator(self.name, **kwargs)(
                self.validator
            )
        }

    def __hash__(self) -> int:
        return hash(self._unique_hash)


class OperableModel(BaseModel):

    model_config = ConfigDict(
        extra="forbid",
        arbitrary_types_allowed=True,
        use_enum_values=True,
        populate_by_name=True,
    )

    extra_fields: dict[str, Any] = Field(default_factory=dict)

    @field_serializer("extra_fields")
    def _serialize_extra_fields(
        self,
        value: dict[str, FieldInfo],
    ) -> dict[str, Any]:
        """Custom serializer for extra fields."""
        output_dict = {}
        for k in value.keys():
            k_value = self.__dict__.get(k)
            output_dict[k] = k_value
        return output_dict

    @field_validator("extra_fields")
    def _validate_extra_fields(
        cls,
        value: dict[str, dict | FieldInfo | FieldModel],
    ) -> dict[str, FieldInfo]:
        """Custom validator for extra fields."""
        if not isinstance(value, dict):
            raise LionValueError("Extra fields must be a dictionary")

        out_ = {}
        for k, v in value.items():
            v = v.to_dict() if isinstance(v, FieldModel) else v
            out_[k] = Field(**v) if isinstance(v, dict) else v

        return out_

    @property
    def all_fields(self) -> dict[str, FieldInfo]:
        """
        Get all fields including model fields and extra fields.

        Returns:
            dict[str, FieldInfo]: A dictionary containing all fields.
        """
        return {**self.model_fields, **self.extra_fields}

    def add_field(
        self,
        field_name: FIELD_NAME,
        /,
        value: Any = LN_UNDEFINED,
        annotation: type = LN_UNDEFINED,
        field_obj: FieldInfo = LN_UNDEFINED,
        field_model: FieldModel = LN_UNDEFINED,
        **kwargs,
    ) -> None:
        """
        Add a new field to the component's extra fields.

        Args:
            field_name: The name of the field to add.
            value: The value of the field.
            annotation: Type annotation for the field.
            field_obj: A pre-configured FieldInfo object.
            **kwargs: Additional keyword arguments for Field configuration.

        Raises:
            LionValueError: If the field already exists.
        """
        if field_name in self.all_fields:
            raise LionValueError(f"Field '{field_name}' already exists")

        self.update_field(
            field_name,
            value=value,
            annotation=annotation,
            field_obj=field_obj,
            field_model=field_model,
            **kwargs,
        )

    def update_field(
        self,
        field_name: FIELD_NAME,
        /,
        value: Any = LN_UNDEFINED,
        annotation: type = LN_UNDEFINED,
        field_obj: FieldInfo = LN_UNDEFINED,
        field_model: FieldModel = LN_UNDEFINED,
        **kwargs,
    ) -> None:
        """
        Update an existing field or create a new one if it doesn't exist.

        Args:
            field_name: The name of the field to update or create.
            value: The new value for the field.
            annotation: Type annotation for the field.
            field_obj: A pre-configured FieldInfo object.
            **kwargs: Additional keyword arguments for Field configuration.

        Raises:
            ValueError: If both 'default' and 'default_factory' are
                        provided in kwargs.
        """

        # pydanitc Field object cannot have both default and default_factory
        if "default" in kwargs and "default_factory" in kwargs:
            raise ValueError(
                "Cannot provide both 'default' and 'default_factory'",
            )

        if field_obj and field_model:
            raise ValueError(
                "Cannot provide both 'field_obj' and 'field_model'",
            )

        # handle field_obj
        if field_obj is not LN_UNDEFINED:
            if not isinstance(field_obj, FieldInfo):
                raise ValueError(
                    "Invalid field_obj, should be a pydantic FieldInfo object"
                )
            self.extra_fields[field_name] = field_obj

        if field_model is not LN_UNDEFINED:
            if not isinstance(field_model, FieldModel):
                raise ValueError(
                    "Invalid field_model, should be a FieldModel object"
                )
            self.extra_fields[field_name] = Field(**field_model.to_dict())

        # handle kwargs
        if kwargs:
            if field_name in self.all_fields:  # existing field
                for k, v in kwargs.items():
                    self.field_setattr(field_name, k, v)
            else:
                self.extra_fields[field_name] = Field(**kwargs)

        # handle no explicit defined field
        if field_obj is LN_UNDEFINED and not kwargs:
            if field_name not in self.all_fields:
                self.extra_fields[field_name] = Field()

        field_obj = self.all_fields[field_name]

        # handle annotation
        if annotation is not LN_UNDEFINED:
            field_obj.annotation = annotation
        if not field_obj.annotation:
            field_obj.annotation = Any

        # handle value
        if value is LN_UNDEFINED:
            if getattr(self, field_name, LN_UNDEFINED) is not LN_UNDEFINED:
                value = getattr(self, field_name)

            elif getattr(field_obj, "default") is not PydanticUndefined:
                value = field_obj.default

            elif getattr(field_obj, "default_factory"):
                value = field_obj.default_factory()

        setattr(self, field_name, value)

    # field management methods
    def field_setattr(
        self,
        field_name: FIELD_NAME,
        attr: str,
        value: Any,
        /,
    ) -> None:
        """Set the value of a field attribute."""
        all_fields = self.all_fields
        if field_name not in all_fields:
            raise KeyError(f"Field {field_name} not found in object fields.")
        field_obj = all_fields[field_name]
        if hasattr(field_obj, attr):
            setattr(field_obj, attr, value)
        else:
            if not isinstance(field_obj.json_schema_extra, dict):
                field_obj.json_schema_extra = {}
            field_obj.json_schema_extra[attr] = value

    def field_hasattr(
        self,
        field_name: FIELD_NAME,
        attr: str,
        /,
    ) -> bool:
        """Check if a field has a specific attribute."""
        all_fields = self.all_fields
        if field_name not in all_fields:
            raise KeyError(f"Field {field_name} not found in object fields.")
        field_obj = all_fields[field_name]
        if hasattr(field_obj, attr):
            return True
        elif isinstance(field_obj.json_schema_extra, dict):
            if field_name in field_obj.json_schema_extra:
                return True
        else:
            return False

    def field_getattr(
        self,
        field_name: FIELD_NAME,
        attr: str,
        default: Any = LN_UNDEFINED,
        /,
    ) -> Any:
        """Get the value of a field attribute."""
        all_fields = self.all_fields

        if field_name not in all_fields:
            raise KeyError(f"Field {field_name} not found in object fields.")

        if str(attr).strip("s").lower() == "annotation":
            return self.model_fields[field_name].annotation

        field_obj = all_fields[field_name]

        # check fieldinfo attr
        value = getattr(field_obj, attr, LN_UNDEFINED)
        if value is not LN_UNDEFINED:
            return value
        else:
            if isinstance(field_obj.json_schema_extra, dict):
                value = field_obj.json_schema_extra.get(attr, LN_UNDEFINED)
                if value is not LN_UNDEFINED:
                    return value

        # undefined attr
        if default is not LN_UNDEFINED:
            return default
        else:
            raise AttributeError(
                f"field {field_name} has no attribute {attr}",
            )
