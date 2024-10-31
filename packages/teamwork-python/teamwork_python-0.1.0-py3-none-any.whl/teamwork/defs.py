from abc import ABC
from enum import Enum
from typing import Dict, Optional, TypeAlias

from pydantic import BaseModel, Field

TbId: TypeAlias = int


class ReceiverType(Enum):
    "The type of receiver for the message."

    USER = 0
    GROUP = 1


class User(BaseModel):
    "The user object of Teamwork"

    model_config = {
        # allow populate model by python naming convention
        "populate_by_name": True,
    }
    username: str = Field(..., description="The user's username (email address)")
    display_name: str = Field(..., alias="displayName", description="The user's display name")
    tb_id: TbId = Field(..., alias="tbId", description="The user's unique tbId")
    custom_fields: Optional[Dict] = Field(default=None, alias="customFields", description="The user's custom fields")
    profile_pic: Optional[str] = Field(
        default=None, alias="profilePic", description="The url of user's profile picture"
    )
    properties: Optional[Dict] = Field(default=None, description="The user's server properties")


class TeamworkAbstractClient(ABC):
    def __init__(self, endpoint: str, api_token: str):
        self.endpoint = endpoint
        self.api_token = api_token
