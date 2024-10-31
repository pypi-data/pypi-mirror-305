from pydantic import BaseModel, ConfigDict
from pydantic.fields import FieldInfo

from lion_core.protocols.fields.action_requests_ import ACTION_REQUESTS_FIELD
from lion_core.protocols.fields.action_required_ import ACTION_REQUIRED_FIELD
from lion_core.protocols.fields.action_responses_ import ACTION_RESPONSES_FIELD
from lion_core.protocols.fields.reason_ import REASON_FIELD
from lion_core.protocols.models import FieldModel

from .utils import PrepFieldParamsModel


class Step:

    @staticmethod
    def as_request_model_type(
        reason: bool = False,
        actions: bool = False,
        exclude_fields: set | list = None,
        include_fields: set | list = None,
        operative_model: type[BaseModel] | None = None,
        config_dict: ConfigDict | None = None,
        doc: str | None = None,
        validators=None,
        use_base_kwargs: bool = False,
        inherit_base: bool = True,
        field_descriptions: dict[str, str] | None = None,
        frozen: bool = False,
        extra_fields: dict[str, FieldInfo] | None = None,
        use_all_fields: bool = False,
        field_models: list[FieldModel] | None = None,
    ):

        include_fields = include_fields or []
        field_models = field_models or []

        if not isinstance(include_fields, list):
            include_fields = list(include_fields)

        if reason:
            field_models.append(REASON_FIELD)

        if actions:
            field_models.append(ACTION_REQUIRED_FIELD)
            field_models.append(ACTION_REQUESTS_FIELD)
            field_models.append(ACTION_RESPONSES_FIELD)

        params = PrepFieldParamsModel.as_request_model_type(
            exclude_fields=exclude_fields,
            include_fields=include_fields,
            base=operative_model,
            config_dict=config_dict,
            doc=doc,
            validators=validators,
            use_base_kwargs=use_base_kwargs,
            inherit_base=inherit_base,
            field_descriptions=field_descriptions,
            frozen=frozen,
            extra_fields=extra_fields,
            use_all_fields=use_all_fields,
            field_models=field_models,
        )
        return params

    @staticmethod
    def as_response_model_type(
        request_params: PrepFieldParamsModel,
        return_fields: dict | list = None,
        response_validators: dict = None,
        frozen_reponse: bool = False,
        response_config_dict=None,
        response_doc=None,
    ) -> PrepFieldParamsModel:

        field_models = []
        if request_params.request_model.action_required:
            field_models.append(ACTION_RESPONSES_FIELD)

        params = PrepFieldParamsModel.as_response_model_type(
            request_params=request_params,
            field_models=field_models,
            return_fields=return_fields,
            response_validators=response_validators,
            frozen=frozen_reponse,
            response_config_dict=response_config_dict,
            response_doc=response_doc,
        )
        return params

    @staticmethod
    def parse_request_to_response_model(
        request_params: PrepFieldParamsModel,
        data: dict,
        return_fields: dict | list = None,
        response_validators: dict = None,
        frozen_reponse: bool = False,
        response_config_dict=None,
        response_doc=None,
    ) -> BaseModel:
        params = Step.as_response_model_type(
            request_params=request_params,
            return_fields=return_fields,
            response_validators=response_validators,
            frozen_reponse=frozen_reponse,
            response_config_dict=response_config_dict,
            response_doc=response_doc,
        )
        return params.response_model_type.model_validate(data)
