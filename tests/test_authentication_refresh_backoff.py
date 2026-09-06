"""authentication_refresh must back off on RESOURCE_EXHAUSTED, not surface the first one."""
import asyncio
from unittest.mock import AsyncMock, MagicMock

import grpc
import pytest
from grpc import StatusCode

import lucidmotors
from tenacity import wait_none
from lucidmotors.gen import login_session_pb2


class _RpcError(grpc.aio.AioRpcError):
    def __init__(self, code):
        super().__init__(code, grpc.aio.Metadata(), grpc.aio.Metadata(), details="", debug_error_string="")


def _session_reply():
    reply = login_session_pb2.GetNewJWTTokenResponse()
    reply.session_info.id_token = "id"
    reply.session_info.gigya_jwt = "g"
    reply.session_info.refresh_token = "r"
    reply.session_info.expiry_time_sec = 2_000_000_000  # int32 field; 4e9 overflows
    return reply


def _api_with_login_service(side_effects):
    api = lucidmotors.LucidAPI.__new__(lucidmotors.LucidAPI)
    api._refresh_token = "r"
    api._interceptor = MagicMock()
    api._login_service = MagicMock()
    api._login_service.GetNewJWTToken = AsyncMock(side_effect=side_effects)
    return api


def test_retries_then_succeeds():
    api = _api_with_login_service([_RpcError(StatusCode.RESOURCE_EXHAUSTED),
                                   _RpcError(StatusCode.RESOURCE_EXHAUSTED),
                                   _session_reply()])
    no_wait = lucidmotors.LucidAPI.authentication_refresh.retry_with(wait=wait_none())
    asyncio.run(no_wait(api))
    assert api._login_service.GetNewJWTToken.await_count == 3
    assert api._refresh_token == "r"


def test_gives_up_after_four_attempts():
    api = _api_with_login_service([_RpcError(StatusCode.RESOURCE_EXHAUSTED)] * 4)
    no_wait = lucidmotors.LucidAPI.authentication_refresh.retry_with(wait=wait_none())
    with pytest.raises(Exception):
        asyncio.run(no_wait(api))
    assert api._login_service.GetNewJWTToken.await_count == 4


def test_non_rate_limit_error_is_not_retried():
    api = _api_with_login_service([_RpcError(StatusCode.UNAUTHENTICATED)])
    with pytest.raises(lucidmotors.exceptions.APIError):
        asyncio.run(api.authentication_refresh())
    assert api._login_service.GetNewJWTToken.await_count == 1
