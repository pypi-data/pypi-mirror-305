# aiomatter/bot.py

import asyncio
from logging import Logger
from typing import Any, Callable, Coroutine, Dict, List

from .driver import MattermostDriver
from .events import EventType
from .plugin import Plugin
from .settings import Settings
from .aiologger import setup_logger


EventHandler = Callable[[Dict[str, Any]], Coroutine[Any, Any, None]]


class Bot:
    def __init__(
        self,
        plugins: List[Plugin],
        settings: Settings,
        logger: Logger | None = None
    ):
        """Инициализация бота с подключенными плагинами и настройками."""
        self.plugins = plugins
        self.settings = settings
        self.logger = logger or setup_logger()
        self.driver = MattermostDriver(
            settings.full_api_url, settings.BOT_TOKEN, logger=self.logger
        )
        self.handlers: Dict[EventType, List[EventHandler]] = (
            self._register_plugins()
        )

    def _register_plugins(self) -> Dict[EventType, List[EventHandler]]:
        """Регистрирует плагины и передает им драйвер."""
        handlers: Dict[EventType, List[EventHandler]] = {}
        for plugin in self.plugins:
            plugin.setup_plugin(self.driver, self.logger)
            for event_type, funcs in plugin.get_handlers().items():
                handlers.setdefault(event_type, []).extend(funcs)
        return handlers

    async def _initialize(self) -> None:
        await self.driver.initialize()

    async def handle_event(self, event: Dict[str, Any]):
        """Обрабатывает событие и вызывает соответствующие хэндлеры."""
        try:
            event_type = event.get('event')
            if event_type in self.handlers:
                for handler in self.handlers[event_type]:
                    await handler(event)
        except Exception as e:
            self.logger.info(f"Ошибка при обработке события: {e}")

    async def _async_run(self):
        """Асинхронный метод запуска бота."""
        await self._initialize()

        ws_url = f"{self.settings.full_api_url}/websocket"
        self.logger.info(f"Бот подключается к WebSocket: {ws_url}")

        while True:
            try:
                await self.driver.connect_websocket(ws_url, self.handle_event)
            except Exception as e:
                self.logger.error(
                    f"Ошибка WebSocket: {e}. Переподключение через 5 секунд..."
                )
                await asyncio.sleep(5)

    def run(self):
        """Синхронный метод запуска бота."""
        asyncio.run(self._async_run())

    async def _async_stop(self):
        """Асинхронная остановка бота."""
        await self.driver.close()

    def stop(self):
        """Синхронный метод для остановки бота."""
        asyncio.run(self._async_stop())
