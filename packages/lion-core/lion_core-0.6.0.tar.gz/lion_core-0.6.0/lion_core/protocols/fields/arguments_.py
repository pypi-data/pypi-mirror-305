from lionfuncs import to_dict

from lion_core.protocols.models import FieldModel

_arguments_description = (
    "Provide the arguments to pass to the function as a "
    "dictionary. **Use "
    "argument names and types as specified in the "
    "`tool_schemas`; do not "
    "invent argument names.**"
)


def validate_arguments(cls, value):
    return to_dict(
        value,
        fuzzy_parse=True,
        suppress=True,
        recursive=True,
    )


ARGUMENTS_FIELD = FieldModel(
    name="arguments",
    annotation=dict,
    default_factory=dict,
    title="Action Arguments",
    description=_arguments_description,
    examples=[{"num1": 1, "num2": 2}, {"x": "hello", "y": "world"}],
    validator=validate_arguments,
    validator_kwargs={"mode": "before"},
)
