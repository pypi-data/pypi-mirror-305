import logging
from typing import Any
import copy


class NoExceptionStreamHandler(logging.StreamHandler[Any]):
    def emit(self, record: logging.LogRecord) -> Any:
        record = copy.copy(record)
        # Clear exc_info to disable exception output for this handler only
        record.exc_info = None
        super().emit(record)
