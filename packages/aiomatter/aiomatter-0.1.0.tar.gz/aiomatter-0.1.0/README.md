
# Aiomatter Bot

Aiomatter is a Python library for creating a bot that interacts with Mattermost via its API and WebSocket. This README provides instructions on setting up the bot and an example of a greeting plugin.

## Table of Contents
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Bot](#running-the-bot)
- [Example Greeting Plugin](#example-greeting-plugin)
- [License](#license)
- [Author](#author)

## Installation

To install Aiomatter, use pip:

```
pip install aiomatter
```

## Configuration

To configure the bot, you need to create a settings object with the following parameters:

- `bot_token`: Your Mattermost bot token.
- `base_url`: The base URL of your Mattermost server.
- `api_path`: The API path (default is `/api/v4`).

Example:

```
from aiomatter.settings import Settings

settings = Settings(
    bot_token='your_bot_token',
    base_url='https://chat.yourserver.com',
    api_path='/api/v4'
)
```

## Running the Bot

To run the bot, create an instance of the `Bot` class and call the `run` method:

```
from aiomatter.bot import Bot
from aiomatter.settings import Settings
from plugins import MyPlugin  # Your plugin

def get_bot() -> Bot:
    settings = Settings(
        bot_token='your_bot_token',
        base_url='https://chat.yourserver.com',
        api_path='/api/v4'
    )
    
    plugins = [MyPlugin()]

    return Bot(settings=settings, plugins=plugins)

if __name__ == '__main__':
    bot = get_bot()
    bot.run()
```

## Example Greeting Plugin

The following example demonstrates a simple greeting plugin that responds to the `POSTED` event.

```plugin.py
from aiomatter.plugin import Plugin
from aiomatter.wrappers import listen
from aiomatter.events import EventType
from aiomatter.schemas.events import PostEvent

class MyPlugin(Plugin):

    @listen(EventType.POSTED)
    async def hello(self, event: PostEvent):
        channel_id = event.data.post.channel_id  # Access channel_id from the typed event
        if channel_id:
            await self.driver.send_message(
                channel_id=channel_id,
                message='Hello!'
            )
            self.logger.info(f"Message sent to channel {channel_id}.")
```

### Note on Typing

In the plugin methods, the decorator processes the event and returns a typed event instead of a generic event. This enhances type safety and improves code readability.

## License

This project is licensed under the MIT License.

## Author

Vladimir Savelev - [GitHub Profile](https://github.com/savvlex)
