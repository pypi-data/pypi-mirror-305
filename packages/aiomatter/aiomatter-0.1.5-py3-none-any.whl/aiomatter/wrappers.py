import json
from aiomatter.schemas.post_events import PostEvent, EditEvent, DeleteEvent
from aiomatter.events import EventType

EVENT_MAPPING = {
    EventType.POSTED: PostEvent,
    EventType.POST_EDITED: EditEvent,
    EventType.POST_DELETED: DeleteEvent,
    EventType.ANY: lambda event: event,
}


def listen(event_type: EventType, ignore_bots: bool = True):
    """Декоратор для регистрации обработчиков событий."""

    def decorator(func):
        async def wrapper(plugin, event):
            post_data = json.loads(event['data'].get('post', '{}'))
            sender = post_data.get('sender_name', None)
            props = post_data.get('props', {})
            from_bot = props.get('from_bot', 'false')

            if (from_bot == 'true' or sender == 'System') and ignore_bots:
                return

            event_class = EVENT_MAPPING.get(event_type)
            if not event_class:
                raise ValueError(f"Неизвестный тип события: {event_type}")

            if event_type == EventType.ANY:
                typed_event = event
            else:
                typed_event = event_class(**event)

            await func(plugin, typed_event)

        wrapper.event_type = event_type
        return wrapper

    return decorator
