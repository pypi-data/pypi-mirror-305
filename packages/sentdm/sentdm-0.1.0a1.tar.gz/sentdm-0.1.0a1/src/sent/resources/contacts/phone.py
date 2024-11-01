# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.shared.contact import Contact

__all__ = ["PhoneResource", "AsyncPhoneResource"]


class PhoneResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PhoneResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-python#accessing-raw-response-data-eg-headers
        """
        return PhoneResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhoneResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-python#with_streaming_response
        """
        return PhoneResourceWithStreamingResponse(self)

    def retrieve(
        self,
        phone_number: str,
        *,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Contact:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._get(
            f"/contact/{customer_id}/phone/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Contact,
        )


class AsyncPhoneResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPhoneResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPhoneResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhoneResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-python#with_streaming_response
        """
        return AsyncPhoneResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        phone_number: str,
        *,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Contact:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._get(
            f"/contact/{customer_id}/phone/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Contact,
        )


class PhoneResourceWithRawResponse:
    def __init__(self, phone: PhoneResource) -> None:
        self._phone = phone

        self.retrieve = to_raw_response_wrapper(
            phone.retrieve,
        )


class AsyncPhoneResourceWithRawResponse:
    def __init__(self, phone: AsyncPhoneResource) -> None:
        self._phone = phone

        self.retrieve = async_to_raw_response_wrapper(
            phone.retrieve,
        )


class PhoneResourceWithStreamingResponse:
    def __init__(self, phone: PhoneResource) -> None:
        self._phone = phone

        self.retrieve = to_streamed_response_wrapper(
            phone.retrieve,
        )


class AsyncPhoneResourceWithStreamingResponse:
    def __init__(self, phone: AsyncPhoneResource) -> None:
        self._phone = phone

        self.retrieve = async_to_streamed_response_wrapper(
            phone.retrieve,
        )
