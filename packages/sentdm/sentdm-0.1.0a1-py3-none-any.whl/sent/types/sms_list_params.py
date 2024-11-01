# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SMSListParams"]


class SMSListParams(TypedDict, total=False):
    phone_number: Required[Annotated[str, PropertyInfo(alias="phoneNumber")]]

    retrieve_if_does_not_exists: Required[Annotated[bool, PropertyInfo(alias="retrieveIfDoesNotExists")]]

    sent_id: Annotated[Optional[str], PropertyInfo(alias="sentId")]
