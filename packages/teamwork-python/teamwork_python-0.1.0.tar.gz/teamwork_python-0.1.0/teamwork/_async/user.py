from typing import Dict

import aiohttp

from ..defs import TbId, TeamworkAbstractClient, User


class UserClient(TeamworkAbstractClient):
    async def by_id(self, tb_id: TbId, fields: Dict = "*", customFields: Dict = "*") -> User:
        """
        Get user profile by their tb_id.

        Args:
            tb_id (int): The ID of the user to retrieve.
            fields (dict): A dictionary of fields to include in the response. Default get all.
            customFields (dict): A dictionary of custom fields to include in the response. Default get all.
        Returns:
            User: An instance of the User class populated with the user's data.
        Raises:
            aiohttp.ClientResponseError: If the request fails or the response status is not 200.
        """
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.endpoint}/api/user/{tb_id}",
                params={"apiToken": self.api_token, "fields": fields, "customFields": customFields},
            ) as response:
                res = await response.json()
                if response.status != 200:
                    raise aiohttp.ClientResponseError(
                        response.request_info,
                        response.history,
                        status=response.status,
                        message=res["error"],
                        headers=response.headers,
                    )
                return User(**res["data"])

    async def by_username(self, username: str, fields: Dict = "*", customFields: Dict = "*") -> User:
        """
        Get user profile by username.

        Args:
            username (str): The username of the user whose profile is to be retrieved.
            fields (dict, optional): The fields to be included in the user profile. Defaults to "*".
            customFields (dict, optional): The custom fields to be included in the user profile. Defaults to "*".

        Returns:
            User: An instance of the User class populated with the retrieved user profile data.

        Raises:
            aiohttp.ClientResponseError: If the request fails or the response contains an error.
        """
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.endpoint}/api/user/username",
                params={
                    "apiToken": self.api_token,
                    "username": username,
                    "fields": fields,
                    "customFields": customFields,
                },
            ) as response:
                response.raise_for_status()
                res = await response.json()
                return User(**res["data"])
