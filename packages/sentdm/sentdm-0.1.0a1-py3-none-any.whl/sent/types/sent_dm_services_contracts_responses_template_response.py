# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SentDmServicesContractsResponsesTemplateResponse"]


class SentDmServicesContractsResponsesTemplateResponse(BaseModel):
    id: Optional[str] = None

    category: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    customer_id: Optional[str] = FieldInfo(alias="customerId", default=None)

    name: Optional[str] = None

    raw_body: Optional[str] = FieldInfo(alias="rawBody", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    whatsapp_template_name: Optional[str] = FieldInfo(alias="whatsappTemplateName", default=None)

    whatsapp_template_status: Optional[str] = FieldInfo(alias="whatsappTemplateStatus", default=None)
