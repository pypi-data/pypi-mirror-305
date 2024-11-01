import logging
import os

LOG_FILE_PATH = os.path.join(os.getcwd(), "aiomatter.log")


def setup_logger(
    name: str = "Aiomatter", log_file: str = LOG_FILE_PATH
) -> logging.Logger:
    """Создает и настраивает логгер."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    log_format = logging.Formatter(
        "[%(asctime)s] %(name)s: %(message)s", datefmt="%d.%m.%Y %H:%M:%S"
    )

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(log_format)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.propagate = False

    return logger
