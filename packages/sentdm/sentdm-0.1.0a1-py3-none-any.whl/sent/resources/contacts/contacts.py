# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ...types import contact_list_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["ContactsResource", "AsyncContactsResource"]


class ContactsResource(SyncAPIResource):
    @cached_property
    def id(self) -> IDResource:
        return IDResource(self._client)

    @cached_property
    def phone(self) -> PhoneResource:
        return PhoneResource(self._client)

    @cached_property
    def with_raw_response(self) -> ContactsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-python#accessing-raw-response-data-eg-headers
        """
        return ContactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContactsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-python#with_streaming_response
        """
        return ContactsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        customer_id: str,
        page: int,
        page_size: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/contacts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "customer_id": customer_id,
                        "page": page,
                        "page_size": page_size,
                    },
                    contact_list_params.ContactListParams,
                ),
            ),
            cast_to=object,
        )


class AsyncContactsResource(AsyncAPIResource):
    @cached_property
    def id(self) -> AsyncIDResource:
        return AsyncIDResource(self._client)

    @cached_property
    def phone(self) -> AsyncPhoneResource:
        return AsyncPhoneResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncContactsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContactsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-python#with_streaming_response
        """
        return AsyncContactsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        customer_id: str,
        page: int,
        page_size: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/contacts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "customer_id": customer_id,
                        "page": page,
                        "page_size": page_size,
                    },
                    contact_list_params.ContactListParams,
                ),
            ),
            cast_to=object,
        )


class ContactsResourceWithRawResponse:
    def __init__(self, contacts: ContactsResource) -> None:
        self._contacts = contacts

        self.list = to_raw_response_wrapper(
            contacts.list,
        )

    @cached_property
    def id(self) -> IDResourceWithRawResponse:
        return IDResourceWithRawResponse(self._contacts.id)

    @cached_property
    def phone(self) -> PhoneResourceWithRawResponse:
        return PhoneResourceWithRawResponse(self._contacts.phone)


class AsyncContactsResourceWithRawResponse:
    def __init__(self, contacts: AsyncContactsResource) -> None:
        self._contacts = contacts

        self.list = async_to_raw_response_wrapper(
            contacts.list,
        )

    @cached_property
    def id(self) -> AsyncIDResourceWithRawResponse:
        return AsyncIDResourceWithRawResponse(self._contacts.id)

    @cached_property
    def phone(self) -> AsyncPhoneResourceWithRawResponse:
        return AsyncPhoneResourceWithRawResponse(self._contacts.phone)


class ContactsResourceWithStreamingResponse:
    def __init__(self, contacts: ContactsResource) -> None:
        self._contacts = contacts

        self.list = to_streamed_response_wrapper(
            contacts.list,
        )

    @cached_property
    def id(self) -> IDResourceWithStreamingResponse:
        return IDResourceWithStreamingResponse(self._contacts.id)

    @cached_property
    def phone(self) -> PhoneResourceWithStreamingResponse:
        return PhoneResourceWithStreamingResponse(self._contacts.phone)


class AsyncContactsResourceWithStreamingResponse:
    def __init__(self, contacts: AsyncContactsResource) -> None:
        self._contacts = contacts

        self.list = async_to_streamed_response_wrapper(
            contacts.list,
        )

    @cached_property
    def id(self) -> AsyncIDResourceWithStreamingResponse:
        return AsyncIDResourceWithStreamingResponse(self._contacts.id)

    @cached_property
    def phone(self) -> AsyncPhoneResourceWithStreamingResponse:
        return AsyncPhoneResourceWithStreamingResponse(self._contacts.phone)
