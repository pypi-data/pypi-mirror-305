from typing import Union

from pydantic import Field
from pydantic.dataclasses import dataclass


@dataclass
class UserProps:
    custom_status: Union[str, None] = Field(default=None, alias='customStatus')


@dataclass
class NotifyProps:
    auto_responder_active: Union[str, None] = Field(
        default=None, alias='auto_responder_active'
    )
    auto_responder_message: Union[str, None] = Field(
        default=None, alias='auto_responder_message'
    )
    calls_desktop_sound: Union[str, None] = Field(
        default=None, alias='calls_desktop_sound'
    )
    calls_notification_sound: Union[str, None] = Field(
        default=None, alias='calls_notification_sound'
    )
    channel: Union[str, None] = Field(default=None)
    comments: Union[str, None] = Field(default=None)
    desktop: Union[str, None] = Field(default=None)
    desktop_notification_sound: Union[str, None] = Field(
        default=None, alias='desktop_notification_sound'
    )
    desktop_sound: Union[str, None] = Field(default=None)
    desktop_threads: Union[str, None] = Field(default=None)
    email: Union[str, None] = Field(default=None)
    email_threads: Union[str, None] = Field(default=None)
    first_name: Union[str, None] = Field(default=None, alias='first_name')
    highlight_keys: Union[str, None] = Field(
        default=None, alias='highlight_keys'
    )
    mention_keys: Union[str, None] = Field(default=None, alias='mention_keys')
    push: Union[str, None] = Field(default=None)
    push_status: Union[str, None] = Field(default=None, alias='push_status')
    push_threads: Union[str, None] = Field(default=None)


@dataclass
class Timezone:
    automatic_timezone: Union[str, None] = Field(
        default=None, alias='automaticTimezone'
    )
    manual_timezone: Union[str, None] = Field(
        default=None, alias='manualTimezone'
    )
    use_automatic_timezone: Union[str, None] = Field(
        default=None, alias='useAutomaticTimezone'
    )


@dataclass
class MattermostUser:
    id: str
    create_at: int
    update_at: int
    delete_at: int
    username: str
    auth_data: str
    auth_service: str
    email: str
    nickname: str
    first_name: str
    last_name: str
    roles: str  # Поля без значения по умолчанию идут выше
    locale: str
    disable_welcome_email: bool
    position: Union[str, None] = (
        None  # Поля с значением по умолчанию идут ниже
    )
    props: UserProps = Field(default_factory=UserProps)
    notify_props: NotifyProps = Field(default_factory=NotifyProps)
    last_picture_update: Union[int, None] = None
    timezone: Timezone = Field(default_factory=Timezone)

    class Config:
        populate_by_name = True
