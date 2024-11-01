# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WhatsappPayload"]


class WhatsappPayload(BaseModel):
    id: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    invalid_record: Optional[bool] = FieldInfo(alias="invalidRecord", default=None)

    is_business: Optional[bool] = FieldInfo(alias="isBusiness", default=None)

    number_type: Optional[str] = FieldInfo(alias="numberType", default=None)

    payload: Optional[str] = None

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    profile_picture: Optional[str] = FieldInfo(alias="profilePicture", default=None)

    sent_id: Optional[str] = FieldInfo(alias="sentId", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    whatsapp_id: Optional[str] = FieldInfo(alias="whatsappId", default=None)
