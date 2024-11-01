# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent import Sent, AsyncSent
from tests.utils import assert_matches_type
from sent.types.shared import SentDmServicesContractsDataContactDto

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestID:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Sent) -> None:
        id = client.contact.id.retrieve(
            id="id",
            customer_id="customerId",
        )
        assert_matches_type(SentDmServicesContractsDataContactDto, id, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Sent) -> None:
        response = client.contact.id.with_raw_response.retrieve(
            id="id",
            customer_id="customerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        id = response.parse()
        assert_matches_type(SentDmServicesContractsDataContactDto, id, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Sent) -> None:
        with client.contact.id.with_streaming_response.retrieve(
            id="id",
            customer_id="customerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            id = response.parse()
            assert_matches_type(SentDmServicesContractsDataContactDto, id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.contact.id.with_raw_response.retrieve(
                id="id",
                customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.contact.id.with_raw_response.retrieve(
                id="",
                customer_id="customerId",
            )


class TestAsyncID:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSent) -> None:
        id = await async_client.contact.id.retrieve(
            id="id",
            customer_id="customerId",
        )
        assert_matches_type(SentDmServicesContractsDataContactDto, id, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSent) -> None:
        response = await async_client.contact.id.with_raw_response.retrieve(
            id="id",
            customer_id="customerId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        id = await response.parse()
        assert_matches_type(SentDmServicesContractsDataContactDto, id, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSent) -> None:
        async with async_client.contact.id.with_streaming_response.retrieve(
            id="id",
            customer_id="customerId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            id = await response.parse()
            assert_matches_type(SentDmServicesContractsDataContactDto, id, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.contact.id.with_raw_response.retrieve(
                id="id",
                customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.contact.id.with_raw_response.retrieve(
                id="",
                customer_id="customerId",
            )
