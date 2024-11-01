# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessagePhoneNumberParams"]


class MessagePhoneNumberParams(TypedDict, total=False):
    customer_id: Annotated[str, PropertyInfo(alias="customerId")]

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]

    template_id: Annotated[str, PropertyInfo(alias="templateId")]
