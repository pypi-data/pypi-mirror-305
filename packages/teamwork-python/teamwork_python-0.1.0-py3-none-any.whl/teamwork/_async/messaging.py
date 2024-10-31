from typing import Dict

import aiohttp

from ..defs import ReceiverType, TeamworkAbstractClient


class MessagingClient(TeamworkAbstractClient):
    async def send_text(self, text: str, receiver_id: int, receiver_type: ReceiverType) -> Dict:
        """
        Sends a text message to a specified user or group chat asynchronously.
        Args:
            receiver_id (int): The tb_id of the receiver (user or group).
            receiver_type (ReceiverType): The type of the receiver (e.g., user, group).
            text (str): The text message to be sent.
        Returns:
            dict: The response from the server as a dictionary.
        Raises:
            aiohttp.ClientResponseError: If the response status is not 200, raises an error with the response details.
        """

        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.endpoint}/api/message/sendMsg",
                params={
                    "apiToken": self.api_token,
                    "receiverId": receiver_id,
                    "receiverType": receiver_type,
                    "textContent": text,
                },
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
                return res["data"]

    async def send_typing_signal(self, receiver_id: int, receiver_type: ReceiverType) -> Dict:
        """
        Sends a 'is typing' signal to a specified user or group chat asynchronously.
        Args:
            receiver_id (int): The tb_id of the receiver (user or group).
            receiver_type (ReceiverType): The type of the receiver (e.g., user, group).
        Returns:
            dict: The response from the server as a dictionary.
        Raises:
            aiohttp.ClientResponseError: If the response status is not 200, raises an error with the response details.
        """

        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.endpoint}/api/message/sendMsg",
                params={
                    "apiToken": self.api_token,
                    "receiverId": receiver_id,
                    "receiverType": receiver_type,
                    "isTyping": "true",
                },
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
                return res["data"]
