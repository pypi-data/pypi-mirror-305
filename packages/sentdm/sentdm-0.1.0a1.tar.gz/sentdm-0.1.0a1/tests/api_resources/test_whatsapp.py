# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent import Sent, AsyncSent
from sent.types import WhatsappPayload
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWhatsapp:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Sent) -> None:
        whatsapp = client.whatsapp.list(
            phone_number="phoneNumber",
            retrieve_if_does_not_exists=True,
        )
        assert_matches_type(WhatsappPayload, whatsapp, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Sent) -> None:
        whatsapp = client.whatsapp.list(
            phone_number="phoneNumber",
            retrieve_if_does_not_exists=True,
            sent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WhatsappPayload, whatsapp, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Sent) -> None:
        response = client.whatsapp.with_raw_response.list(
            phone_number="phoneNumber",
            retrieve_if_does_not_exists=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whatsapp = response.parse()
        assert_matches_type(WhatsappPayload, whatsapp, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Sent) -> None:
        with client.whatsapp.with_streaming_response.list(
            phone_number="phoneNumber",
            retrieve_if_does_not_exists=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whatsapp = response.parse()
            assert_matches_type(WhatsappPayload, whatsapp, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWhatsapp:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncSent) -> None:
        whatsapp = await async_client.whatsapp.list(
            phone_number="phoneNumber",
            retrieve_if_does_not_exists=True,
        )
        assert_matches_type(WhatsappPayload, whatsapp, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSent) -> None:
        whatsapp = await async_client.whatsapp.list(
            phone_number="phoneNumber",
            retrieve_if_does_not_exists=True,
            sent_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(WhatsappPayload, whatsapp, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSent) -> None:
        response = await async_client.whatsapp.with_raw_response.list(
            phone_number="phoneNumber",
            retrieve_if_does_not_exists=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        whatsapp = await response.parse()
        assert_matches_type(WhatsappPayload, whatsapp, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSent) -> None:
        async with async_client.whatsapp.with_streaming_response.list(
            phone_number="phoneNumber",
            retrieve_if_does_not_exists=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            whatsapp = await response.parse()
            assert_matches_type(WhatsappPayload, whatsapp, path=["response"])

        assert cast(Any, response.is_closed) is True
