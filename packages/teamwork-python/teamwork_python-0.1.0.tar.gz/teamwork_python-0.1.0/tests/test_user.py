import pytest

from teamwork import User
from teamwork._async.client import AsyncClient


@pytest.mark.asyncio
async def test_get_user_by_id(bot_user: User):
    client = AsyncClient()
    user = await client.user.by_id(bot_user.tb_id)
    assert user is not None


@pytest.mark.asyncio
async def test_get_user_by_username(bot_user: User):
    client = AsyncClient()
    user = await client.user.by_username(bot_user.username)
    assert user is not None
