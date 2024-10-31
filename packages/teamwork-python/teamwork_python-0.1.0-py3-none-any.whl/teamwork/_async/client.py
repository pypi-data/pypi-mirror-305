import os

from ..defs import TeamworkAbstractClient
from .messaging import MessagingClient
from .user import UserClient


class AsyncClient(TeamworkAbstractClient):
    """Teamwork python async client"""

    def __init__(self, endpoint: str = None, api_token: str = None):
        if not endpoint:
            endpoint = os.getenv("TEAMWORK_API_ENDPOINT")
            if not endpoint:
                raise ValueError("endpoint is required")
        if not api_token:
            api_token = os.getenv("TEAMWORK_API_KEY")
            if not api_token:
                raise ValueError("api_token is required")

        super().__init__(endpoint, api_token)

        self.user = UserClient(endpoint, api_token)
        self.message = MessagingClient(endpoint, api_token)
