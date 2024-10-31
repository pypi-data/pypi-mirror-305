# aiomatter/plugin.py

from aiomatter.driver import MattermostDriver


class Plugin:
    def __init__(self):
        self.driver: MattermostDriver = None
        self.logger: Logger = None
        self.handlers = self._load_handlers()

    def _load_handlers(self):
        """Собирает все методы-обработчики с декораторами."""
        handlers = {}
        for attr_name in dir(self):
            attr = getattr(self, attr_name)
            if callable(attr) and hasattr(attr, 'event_type'):
                event_type = attr.event_type
                handlers.setdefault(event_type, []).append(attr)
        return handlers

    def setup_plugin(self, driver, logger):
        """Устанавливает драйвер для плагина."""
        self.driver = driver
        self.logger = logger

    def get_handlers(self):
        """Возвращает все зарегистрированные обработчики."""
        return self.handlers
