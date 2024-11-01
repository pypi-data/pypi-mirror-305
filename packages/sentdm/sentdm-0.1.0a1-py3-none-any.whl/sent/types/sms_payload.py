# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SMSPayload"]


class SMSPayload(BaseModel):
    id: Optional[str] = None

    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    national_format: Optional[str] = FieldInfo(alias="nationalFormat", default=None)

    payload: Optional[str] = None

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)

    sent_id: Optional[str] = FieldInfo(alias="sentId", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    valid_number: Optional[bool] = FieldInfo(alias="validNumber", default=None)
