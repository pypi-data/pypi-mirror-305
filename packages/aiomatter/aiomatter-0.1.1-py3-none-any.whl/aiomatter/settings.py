# aimatter/settings.py


class Settings:
    def __init__(
        self, bot_token: str, base_url: str, api_path: str = "/api/v4"
    ):
        """Инициализация параметров конфигурации с автоматической заменой схемы."""
        self.BOT_TOKEN = bot_token
        self.BASE_URL = self._transform_base_url(base_url.rstrip('/'))
        self.API_PATH = api_path

    @staticmethod
    def _transform_base_url(base_url: str) -> str:
        """Заменяет http/https на ws/wss в URL."""
        if base_url.startswith("https://"):
            return base_url.replace("https://", "wss://", 1)
        elif base_url.startswith("http://"):
            return base_url.replace("http://", "ws://", 1)
        else:
            raise ValueError(
                "Некорректная схема URL. Ожидается http:// или https://"
            )

    @property
    def full_api_url(self) -> str:
        """Возвращает полный URL для API."""
        return f"{self.BASE_URL}{self.API_PATH}"
