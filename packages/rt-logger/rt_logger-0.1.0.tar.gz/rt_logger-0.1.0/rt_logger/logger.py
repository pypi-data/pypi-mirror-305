from logging.handlers import RotatingFileHandler
import logging
from typing import Dict
import colorama
from .custom_logger import CustomLogger
from .level_based_formater import LevelBasedFormatter
from .stream_handler import NoExceptionStreamHandler

colorama.init(autoreset=True)


def get_logger(name: str) -> CustomLogger:
    max_filesize_in_mbs = 2_000
    log_filename = "logs.log"
    file_encoding = "UTF-8"

    logger = CustomLogger(name)

    level_formats: Dict[int, str] = {
        logging.DEBUG: "[.] %(message)s",
        logging.INFO: "[+] %(message)s",
        logging.WARNING: "[*] %(message)s",
        logging.ERROR: "[-] %(message)s",
        logging.CRITICAL: "[!] %(message)s",
    }

    level_based_fmt = LevelBasedFormatter(
        "[+] %(message)s", level_formats=level_formats
    )
    console_handler = NoExceptionStreamHandler()
    console_handler.setFormatter(level_based_fmt)

    file_handler = RotatingFileHandler(
        log_filename,
        mode="a",
        maxBytes=max_filesize_in_mbs * 1024 * 1024,
        backupCount=2,
        encoding=file_encoding,
        delay=False,
    )
    file_logging_fmt = logging.Formatter(
        "[%(asctime)s - %(levelname)-8s - %(filename)s - %(lineno)-4s - %(message)s"
    )
    file_logging_fmt = logging.Formatter(
        "%(asctime)s - %(levelname)-8s - [%(filename)s:%(lineno)s] - %(name)s - %(message)s"
    )
    file_handler.setFormatter(file_logging_fmt)

    # Log level of logger should always be DEBUG
    logger.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)
    console_handler.setLevel(logging.DEBUG)

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
