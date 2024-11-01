import json
from typing import Any, Dict, Union

from pydantic import Field, field_validator
from pydantic.dataclasses import dataclass

from aiomatter.events import EventType


@dataclass
class Post:
    id: str
    create_at: int
    update_at: int
    edit_at: int
    delete_at: int
    is_pinned: bool
    user_id: str
    channel_id: str
    root_id: str
    original_id: str
    message: str
    type: str
    hashtags: str
    pending_post_id: str
    reply_count: int
    last_reply_at: int
    remote_id: str | None = None
    props: Dict[str, Any] = Field(default_factory=dict)
    participants: Union[None, Any] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)


@dataclass
class BaseEventData:
    post: Union[Post, str]

    @field_validator("post", mode="before")
    @classmethod
    def parse_post(cls, value: Union[str, Dict[str, Any]]) -> Post:
        """Если 'post' передан как строка, парсим его в объект."""
        if isinstance(value, str):
            try:
                post_data = json.loads(value)
                return Post(**post_data)
            except json.JSONDecodeError:
                raise ValueError("Invalid JSON in 'post' field")
        elif isinstance(value, dict):
            return Post(**value)
        else:
            raise ValueError(f"Invalid type for 'post': {type(value)}")


@dataclass
class DeleteEventData(BaseEventData):
    delete_by: str


@dataclass
class PostEventData(BaseEventData):
    channel_display_name: str
    channel_name: str
    channel_type: str
    sender_name: str
    set_online: bool
    team_id: str


@dataclass
class PostEvent:
    event: EventType
    seq: int
    data: PostEventData
    broadcast: Dict[str, Any] = Field(default_factory=dict)


@dataclass
class EditEvent:
    event: EventType
    seq: int
    data: BaseEventData
    broadcast: Dict[str, Any] = Field(default_factory=dict)


@dataclass
class DeleteEvent:
    event: EventType
    seq: int
    data: DeleteEventData
    broadcast: Dict[str, Any] = Field(default_factory=dict)
