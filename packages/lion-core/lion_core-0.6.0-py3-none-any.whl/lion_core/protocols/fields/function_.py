from lionfuncs import to_dict

from lion_core.protocols.models import FieldModel

_description = (
    "Specify the name of the function to execute. **Choose "
    "from the provided `tool_schemas`; do not invent function names.**"
    "Only provide function names if tool_schemas are provided. Otherwise, "
    "must leave blank or set to None."
)


def validate_args(cls, value):
    return to_dict(value, fuzzy_parse=True)


FUNCTION_FIELD = FieldModel(
    name="function",
    default=None,
    annotation=str | None,
    title="Function",
    description=_description,
    examples=["add", "multiply", "divide"],
    validator=validate_args,
)


__all__ = ["FUNCTION_FIELD"]
