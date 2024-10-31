<img src="https://teamwork.app/static/teamwork_logo_word-7f2b02a09653c972fd5a9e80ea6abbf2.svg" alt="Teamwork Logo" width="400"/>

# Teamwork Python Bot-framework SDK

The official [Teamwork](https://teamwork.app) python bot-framework SDK.

## Installation

Install the packages using pip:

```sh
pip install teamwork-python
```

## Pre-requisites

Before you start, you need to create a bot on your Teamwork app console platform and get the API token.

## Usage

You can use the SDK to interact with the Teamwork Bot-framework API.

### Get user profile

```python
from teamwork import AsyncClient

client = AsyncClient("ENDPOINT_URL", "API_TOKEN")

# by id
user = await client.user.by_id(1001)

# by username
user = await client.user.by_username("john.doe@example.com")
```

### Send message

This is to let your bot account send a message to other end-user or group chats.

```python
from teamwork import ReceiverType

# to a user
res = await client.message.send("Hello world!", 1001, ReceiverType.USER)

# to a group chat
res = await client.message.send("Hello everyone!", 59239, ReceiverType.GROUP)

```

Optionally, you can send a "typing" signal to the target, indicating that the bot is typing before you actually send the message

```python
# first, send the signal
res = await client.message.sending_typing_signal(1001, ReceiverType.USER)

# Sometime later, send the actual message
res = await client.message.send("Hello world!", 1001, ReceiverType.USER)

```

## License

This project is licensed under the MIT License.
