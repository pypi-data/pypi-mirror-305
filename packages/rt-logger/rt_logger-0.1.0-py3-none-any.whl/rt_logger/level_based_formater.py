import logging
from typing import Optional, Dict
import colorama


class LevelBasedFormatter(logging.Formatter):
    def __init__(
        self,
        fmt: Optional[str] = None,
        datefmt: Optional[str] = None,
        style: str = "%",
        level_formats: Optional[Dict[int, str]] = None,
    ) -> None:
        super().__init__(fmt, datefmt, style)  # type: ignore
        # If no level_formats are provided, initialize with an empty dict
        self.level_formats: Dict[int, str] = level_formats or {}
        self.colors = {
            logging.DEBUG: colorama.Fore.LIGHTWHITE_EX,
            logging.INFO: colorama.Fore.GREEN + colorama.Style.BRIGHT,
            logging.WARNING: colorama.Fore.YELLOW + colorama.Style.BRIGHT,
            logging.ERROR: colorama.Fore.RED + colorama.Style.BRIGHT,
            logging.CRITICAL: colorama.Fore.WHITE
            + colorama.Style.BRIGHT
            + colorama.Back.RED,
        }
        self.color_reset = colorama.Style.RESET_ALL

    def format(self, record: logging.LogRecord) -> str:
        # Check if there's a format for this level; use it if it exists
        log_fmt = self.level_formats.get(record.levelno, self._fmt)
        formatter = logging.Formatter(log_fmt)

        # Apply color to the message based on log level
        formatted_message = formatter.format(record)
        color_code = self.colors.get(record.levelno, "")
        return f"{color_code}{formatted_message}{self.color_reset}"
