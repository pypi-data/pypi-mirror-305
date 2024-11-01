# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SentDmServicesContractsDataCustomerDtoParam"]


class SentDmServicesContractsDataCustomerDtoParam(TypedDict, total=False):
    id: str

    created_at: Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]

    name: str

    sending_phone_number: Annotated[str, PropertyInfo(alias="sendingPhoneNumber")]

    sms_bearer_token: Annotated[str, PropertyInfo(alias="smsBearerToken")]

    sms_default_webhook_url: Annotated[str, PropertyInfo(alias="smsDefaultWebhookUrl")]

    sms_messaging_profile_id: Annotated[str, PropertyInfo(alias="smsMessagingProfileId")]

    sms_webhook_failover_url: Annotated[str, PropertyInfo(alias="smsWebhookFailoverUrl")]

    updated_at: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAt", format="iso8601")]

    whatsapp_business_associate_id: Annotated[str, PropertyInfo(alias="whatsappBusinessAssociateId")]

    whatsapp_phone_number_id: Annotated[str, PropertyInfo(alias="whatsappPhoneNumberId")]

    whatsapp_system_user_access_token: Annotated[str, PropertyInfo(alias="whatsappSystemUserAccessToken")]
