# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .id import (
    IDResource,
    AsyncIDResource,
    IDResourceWithRawResponse,
    AsyncIDResourceWithRawResponse,
    IDResourceWithStreamingResponse,
    AsyncIDResourceWithStreamingResponse,
)
from .phone import (
    PhoneResource,
    AsyncPhoneResource,
    PhoneResourceWithRawResponse,
    AsyncPhoneResourceWithRawResponse,
    PhoneResourceWithStreamingResponse,
    AsyncPhoneResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ContactResource", "AsyncContactResource"]


class ContactResource(SyncAPIResource):
    @cached_property
    def id(self) -> IDResource:
        return IDResource(self._client)

    @cached_property
    def phone(self) -> PhoneResource:
        return PhoneResource(self._client)

    @cached_property
    def with_raw_response(self) -> ContactResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sent-python#accessing-raw-response-data-eg-headers
        """
        return ContactResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContactResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sent-python#with_streaming_response
        """
        return ContactResourceWithStreamingResponse(self)


class AsyncContactResource(AsyncAPIResource):
    @cached_property
    def id(self) -> AsyncIDResource:
        return AsyncIDResource(self._client)

    @cached_property
    def phone(self) -> AsyncPhoneResource:
        return AsyncPhoneResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncContactResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sent-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContactResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContactResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sent-python#with_streaming_response
        """
        return AsyncContactResourceWithStreamingResponse(self)


class ContactResourceWithRawResponse:
    def __init__(self, contact: ContactResource) -> None:
        self._contact = contact

    @cached_property
    def id(self) -> IDResourceWithRawResponse:
        return IDResourceWithRawResponse(self._contact.id)

    @cached_property
    def phone(self) -> PhoneResourceWithRawResponse:
        return PhoneResourceWithRawResponse(self._contact.phone)


class AsyncContactResourceWithRawResponse:
    def __init__(self, contact: AsyncContactResource) -> None:
        self._contact = contact

    @cached_property
    def id(self) -> AsyncIDResourceWithRawResponse:
        return AsyncIDResourceWithRawResponse(self._contact.id)

    @cached_property
    def phone(self) -> AsyncPhoneResourceWithRawResponse:
        return AsyncPhoneResourceWithRawResponse(self._contact.phone)


class ContactResourceWithStreamingResponse:
    def __init__(self, contact: ContactResource) -> None:
        self._contact = contact

    @cached_property
    def id(self) -> IDResourceWithStreamingResponse:
        return IDResourceWithStreamingResponse(self._contact.id)

    @cached_property
    def phone(self) -> PhoneResourceWithStreamingResponse:
        return PhoneResourceWithStreamingResponse(self._contact.phone)


class AsyncContactResourceWithStreamingResponse:
    def __init__(self, contact: AsyncContactResource) -> None:
        self._contact = contact

    @cached_property
    def id(self) -> AsyncIDResourceWithStreamingResponse:
        return AsyncIDResourceWithStreamingResponse(self._contact.id)

    @cached_property
    def phone(self) -> AsyncPhoneResourceWithStreamingResponse:
        return AsyncPhoneResourceWithStreamingResponse(self._contact.phone)
