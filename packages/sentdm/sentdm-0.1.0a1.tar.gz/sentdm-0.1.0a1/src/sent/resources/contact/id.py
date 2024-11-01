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
from ...types.shared.sent_dm_services_contracts_data_contact_dto import SentDmServicesContractsDataContactDto

__all__ = ["IDResource", "AsyncIDResource"]


class IDResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IDResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sent-python#accessing-raw-response-data-eg-headers
        """
        return IDResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IDResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sent-python#with_streaming_response
        """
        return IDResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SentDmServicesContractsDataContactDto:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/contact/{customer_id}/id/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SentDmServicesContractsDataContactDto,
        )


class AsyncIDResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIDResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/sent-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIDResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIDResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/sent-python#with_streaming_response
        """
        return AsyncIDResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SentDmServicesContractsDataContactDto:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/contact/{customer_id}/id/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SentDmServicesContractsDataContactDto,
        )


class IDResourceWithRawResponse:
    def __init__(self, id: IDResource) -> None:
        self._id = id

        self.retrieve = to_raw_response_wrapper(
            id.retrieve,
        )


class AsyncIDResourceWithRawResponse:
    def __init__(self, id: AsyncIDResource) -> None:
        self._id = id

        self.retrieve = async_to_raw_response_wrapper(
            id.retrieve,
        )


class IDResourceWithStreamingResponse:
    def __init__(self, id: IDResource) -> None:
        self._id = id

        self.retrieve = to_streamed_response_wrapper(
            id.retrieve,
        )


class AsyncIDResourceWithStreamingResponse:
    def __init__(self, id: AsyncIDResource) -> None:
        self._id = id

        self.retrieve = async_to_streamed_response_wrapper(
            id.retrieve,
        )
