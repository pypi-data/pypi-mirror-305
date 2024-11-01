# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..sent_dm_services_contracts_data_sms_payload_dto import SentDmServicesContractsDataSMSPayloadDto
from ..sent_dm_services_contracts_data_whatsapp_payload_dto import SentDmServicesContractsDataWhatsappPayloadDto

__all__ = ["SentDmServicesContractsDataContactDto"]


class SentDmServicesContractsDataContactDto(BaseModel):
    id: Optional[str] = None

    available_channels: Optional[str] = FieldInfo(alias="availableChannels", default=None)

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    customer_id: Optional[str] = FieldInfo(alias="customerId", default=None)

    default_channel: Optional[str] = FieldInfo(alias="defaultChannel", default=None)

    national_format: Optional[str] = FieldInfo(alias="nationalFormat", default=None)

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    sms_payload_dto: Optional[SentDmServicesContractsDataSMSPayloadDto] = FieldInfo(alias="smsPayloadDTO", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    verified: Optional[bool] = None

    whatsapp_payload_dto: Optional[SentDmServicesContractsDataWhatsappPayloadDto] = FieldInfo(
        alias="whatsappPayloadDTO", default=None
    )
