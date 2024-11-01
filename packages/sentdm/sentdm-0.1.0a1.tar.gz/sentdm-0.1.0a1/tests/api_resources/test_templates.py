# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from sent import Sent, AsyncSent
from sent.types import (
    TemplateResponse,
    TemplateListResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTemplates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Sent) -> None:
        template = client.templates.create()
        assert_matches_type(object, template, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Sent) -> None:
        template = client.templates.create(
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert_matches_type(object, template, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Sent) -> None:
        response = client.templates.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(object, template, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Sent) -> None:
        with client.templates.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(object, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Sent) -> None:
        template = client.templates.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TemplateResponse, template, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Sent) -> None:
        response = client.templates.with_raw_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateResponse, template, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Sent) -> None:
        with client.templates.with_streaming_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.templates.with_raw_response.retrieve(
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.templates.with_raw_response.retrieve(
                id="",
                customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_update(self, client: Sent) -> None:
        template = client.templates.update(
            id="id",
        )
        assert_matches_type(object, template, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Sent) -> None:
        template = client.templates.update(
            id="id",
            category="category",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            raw_body="rawBody",
        )
        assert_matches_type(object, template, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Sent) -> None:
        response = client.templates.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(object, template, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Sent) -> None:
        with client.templates.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(object, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.templates.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Sent) -> None:
        template = client.templates.list(
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Sent) -> None:
        response = client.templates.with_raw_response.list(
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Sent) -> None:
        with client.templates.with_streaming_response.list(
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(TemplateListResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Sent) -> None:
        template = client.templates.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, template, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Sent) -> None:
        response = client.templates.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = response.parse()
        assert_matches_type(object, template, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Sent) -> None:
        with client.templates.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = response.parse()
            assert_matches_type(object, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Sent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            client.templates.with_raw_response.delete(
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.templates.with_raw_response.delete(
                id="",
                customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncTemplates:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncSent) -> None:
        template = await async_client.templates.create()
        assert_matches_type(object, template, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncSent) -> None:
        template = await async_client.templates.create(
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert_matches_type(object, template, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncSent) -> None:
        response = await async_client.templates.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(object, template, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncSent) -> None:
        async with async_client.templates.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(object, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSent) -> None:
        template = await async_client.templates.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TemplateResponse, template, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSent) -> None:
        response = await async_client.templates.with_raw_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateResponse, template, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSent) -> None:
        async with async_client.templates.with_streaming_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.templates.with_raw_response.retrieve(
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.templates.with_raw_response.retrieve(
                id="",
                customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncSent) -> None:
        template = await async_client.templates.update(
            id="id",
        )
        assert_matches_type(object, template, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncSent) -> None:
        template = await async_client.templates.update(
            id="id",
            category="category",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            raw_body="rawBody",
        )
        assert_matches_type(object, template, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncSent) -> None:
        response = await async_client.templates.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(object, template, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncSent) -> None:
        async with async_client.templates.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(object, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.templates.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncSent) -> None:
        template = await async_client.templates.list(
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSent) -> None:
        response = await async_client.templates.with_raw_response.list(
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(TemplateListResponse, template, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSent) -> None:
        async with async_client.templates.with_streaming_response.list(
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(TemplateListResponse, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncSent) -> None:
        template = await async_client.templates.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, template, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSent) -> None:
        response = await async_client.templates.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        template = await response.parse()
        assert_matches_type(object, template, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSent) -> None:
        async with async_client.templates.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            template = await response.parse()
            assert_matches_type(object, template, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSent) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `customer_id` but received ''"):
            await async_client.templates.with_raw_response.delete(
                id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                customer_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.templates.with_raw_response.delete(
                id="",
                customer_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
