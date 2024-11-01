# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SentDmServicesContractsDataCustomerDto"]


class SentDmServicesContractsDataCustomerDto(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    name: Optional[str] = None

    sending_phone_number: Optional[str] = FieldInfo(alias="sendingPhoneNumber", default=None)

    sms_bearer_token: Optional[str] = FieldInfo(alias="smsBearerToken", default=None)

    sms_default_webhook_url: Optional[str] = FieldInfo(alias="smsDefaultWebhookUrl", default=None)

    sms_messaging_profile_id: Optional[str] = FieldInfo(alias="smsMessagingProfileId", default=None)

    sms_webhook_failover_url: Optional[str] = FieldInfo(alias="smsWebhookFailoverUrl", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    whatsapp_business_associate_id: Optional[str] = FieldInfo(alias="whatsappBusinessAssociateId", default=None)

    whatsapp_phone_number_id: Optional[str] = FieldInfo(alias="whatsappPhoneNumberId", default=None)

    whatsapp_system_user_access_token: Optional[str] = FieldInfo(alias="whatsappSystemUserAccessToken", default=None)
