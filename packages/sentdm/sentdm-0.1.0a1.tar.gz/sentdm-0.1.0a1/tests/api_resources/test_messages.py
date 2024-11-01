# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent import Sent, AsyncSent
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Sent) -> None:
        message = client.messages.create()
        assert_matches_type(object, message, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Sent) -> None:
        message = client.messages.create(
            contact_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            template_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, message, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Sent) -> None:
        response = client.messages.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(object, message, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Sent) -> None:
        with client.messages.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(object, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_phone_number(self, client: Sent) -> None:
        message = client.messages.phone_number()
        assert_matches_type(object, message, path=["response"])

    @parametrize
    def test_method_phone_number_with_all_params(self, client: Sent) -> None:
        message = client.messages.phone_number(
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            phone_number="phoneNumber",
            template_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, message, path=["response"])

    @parametrize
    def test_raw_response_phone_number(self, client: Sent) -> None:
        response = client.messages.with_raw_response.phone_number()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(object, message, path=["response"])

    @parametrize
    def test_streaming_response_phone_number(self, client: Sent) -> None:
        with client.messages.with_streaming_response.phone_number() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(object, message, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSent) -> None:
        message = await async_client.messages.create()
        assert_matches_type(object, message, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSent) -> None:
        message = await async_client.messages.create(
            contact_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            template_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, message, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSent) -> None:
        response = await async_client.messages.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(object, message, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSent) -> None:
        async with async_client.messages.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(object, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_phone_number(self, async_client: AsyncSent) -> None:
        message = await async_client.messages.phone_number()
        assert_matches_type(object, message, path=["response"])

    @parametrize
    async def test_method_phone_number_with_all_params(self, async_client: AsyncSent) -> None:
        message = await async_client.messages.phone_number(
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            phone_number="phoneNumber",
            template_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, message, path=["response"])

    @parametrize
    async def test_raw_response_phone_number(self, async_client: AsyncSent) -> None:
        response = await async_client.messages.with_raw_response.phone_number()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(object, message, path=["response"])

    @parametrize
    async def test_streaming_response_phone_number(self, async_client: AsyncSent) -> None:
        async with async_client.messages.with_streaming_response.phone_number() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(object, message, path=["response"])

        assert cast(Any, response.is_closed) is True
