import pytest

from teamwork import AsyncClient


@pytest.mark.asyncio
async def test_send_msg(to):
    client = AsyncClient()
    res = await client.message.send_text("Hello!", to["receiver_id"], to["receiver_type"])
    assert res is not None
    assert "messageId" in res
    assert res["messageId"] is not None


@pytest.mark.asyncio
async def test_send_typing_signal(to):
    client = AsyncClient()
    res = await client.message.send_typing_signal(to["receiver_id"], to["receiver_type"])
    assert res is not None
