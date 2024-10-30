import logging
import os

# Путь к файлу логов
LOG_FILE_PATH = os.path.join(os.getcwd(), "aiomatter.log")


def setup_logger(
    name: str = "Aiomatter", log_file: str = LOG_FILE_PATH
) -> logging.Logger:
    """Создает и настраивает логгер."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Формат вывода логов
    log_format = logging.Formatter(
        "[%(asctime)s] %(name)s: %(message)s", datefmt="%d.%m.%Y %H:%M:%S"
    )

    # Обработчик для записи в файл
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(log_format)

    # Обработчик для вывода в консоль
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)

    # Добавляем оба обработчика к логгеру
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Убираем дублирование логов
    logger.propagate = False

    return logger
