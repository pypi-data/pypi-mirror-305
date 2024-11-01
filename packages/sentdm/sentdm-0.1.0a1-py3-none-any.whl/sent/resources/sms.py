# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import sms_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.sms_payload import SMSPayload

__all__ = ["SMSResource", "AsyncSMSResource"]


class SMSResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SMSResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-python#accessing-raw-response-data-eg-headers
        """
        return SMSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SMSResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-python#with_streaming_response
        """
        return SMSResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        phone_number: str,
        retrieve_if_does_not_exists: bool,
        sent_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SMSPayload:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/sms",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "phone_number": phone_number,
                        "retrieve_if_does_not_exists": retrieve_if_does_not_exists,
                        "sent_id": sent_id,
                    },
                    sms_list_params.SMSListParams,
                ),
            ),
            cast_to=SMSPayload,
        )


class AsyncSMSResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSMSResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sentdm/sent-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSMSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSMSResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sentdm/sent-python#with_streaming_response
        """
        return AsyncSMSResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        phone_number: str,
        retrieve_if_does_not_exists: bool,
        sent_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SMSPayload:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/sms",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "phone_number": phone_number,
                        "retrieve_if_does_not_exists": retrieve_if_does_not_exists,
                        "sent_id": sent_id,
                    },
                    sms_list_params.SMSListParams,
                ),
            ),
            cast_to=SMSPayload,
        )


class SMSResourceWithRawResponse:
    def __init__(self, sms: SMSResource) -> None:
        self._sms = sms

        self.list = to_raw_response_wrapper(
            sms.list,
        )


class AsyncSMSResourceWithRawResponse:
    def __init__(self, sms: AsyncSMSResource) -> None:
        self._sms = sms

        self.list = async_to_raw_response_wrapper(
            sms.list,
        )


class SMSResourceWithStreamingResponse:
    def __init__(self, sms: SMSResource) -> None:
        self._sms = sms

        self.list = to_streamed_response_wrapper(
            sms.list,
        )


class AsyncSMSResourceWithStreamingResponse:
    def __init__(self, sms: AsyncSMSResource) -> None:
        self._sms = sms

        self.list = async_to_streamed_response_wrapper(
            sms.list,
        )
