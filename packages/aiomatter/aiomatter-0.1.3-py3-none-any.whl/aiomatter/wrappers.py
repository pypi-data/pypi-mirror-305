import json
from aiomatter.schemas.events import PostEvent, EditEvent, DeleteEvent
from aiomatter.events import EventType

EVENT_MAPPING = {
    EventType.POSTED: PostEvent,
    EventType.POST_EDITED: EditEvent,
    EventType.POST_DELETED: DeleteEvent,
}


def listen(event_type: EventType):
    """Декоратор для регистрации обработчиков событий."""

    def decorator(func):
        async def wrapper(plugin, event):
            post_data = json.loads(event['data'].get('post', '{}'))
            props = post_data.get('props', {})
            from_bot = props.get('from_bot', 'false')

            if from_bot == 'true':
                return

            event_class = EVENT_MAPPING.get(event_type)
            if not event_class:
                raise ValueError(f"Неизвестный тип события: {event_type}")

            typed_event = event_class(**event)
            await func(plugin, typed_event)

        wrapper.event_type = event_type
        return wrapper

    return decorator
