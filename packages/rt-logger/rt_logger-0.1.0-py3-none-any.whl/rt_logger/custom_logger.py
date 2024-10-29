import logging
from typing import Mapping
from types import TracebackType


class CustomLogger(logging.Logger):
    """Add own methods"""

    def debug(
        self,
        msg: object,
        *args: object,
        exc_info: (
            None
            | bool
            | tuple[type[BaseException], BaseException, TracebackType | None]
            | tuple[None, None, None]
            | BaseException
        ) = None,
        stack_info: bool = False,
        stacklevel: int = 1,
        extra: Mapping[str, object] | None = None,
        wait_for_input: bool = False,
    ) -> None:
        super().debug(
            msg,
            *args,
            exc_info=exc_info,
            stack_info=stack_info,
            stacklevel=stacklevel,
            extra=extra,
        )
        if wait_for_input:
            self.wait_for_input()

    def info(
        self,
        msg: object,
        *args: object,
        exc_info: (
            None
            | bool
            | tuple[type[BaseException], BaseException, TracebackType | None]
            | tuple[None, None, None]
            | BaseException
        ) = None,
        stack_info: bool = False,
        stacklevel: int = 1,
        extra: Mapping[str, object] | None = None,
        wait_for_input: bool = False,
    ) -> None:
        super().info(
            msg,
            *args,
            exc_info=exc_info,
            stack_info=stack_info,
            stacklevel=stacklevel,
            extra=extra,
        )
        if wait_for_input:
            self.wait_for_input()

    def error(
        self,
        msg: object,
        *args: object,
        exc_info: (
            None
            | bool
            | tuple[type[BaseException], BaseException, TracebackType | None]
            | tuple[None, None, None]
            | BaseException
        ) = None,
        stack_info: bool = False,
        stacklevel: int = 1,
        extra: Mapping[str, object] | None = None,
        wait_for_input: bool = False,
    ) -> None:
        super().error(
            msg,
            *args,
            exc_info=exc_info,
            stack_info=stack_info,
            stacklevel=stacklevel,
            extra=extra,
        )
        if wait_for_input:
            self.wait_for_input()

    def critical(
        self,
        msg: object,
        *args: object,
        exc_info: (
            None
            | bool
            | tuple[type[BaseException], BaseException, TracebackType | None]
            | tuple[None, None, None]
            | BaseException
        ) = None,
        stack_info: bool = False,
        stacklevel: int = 1,
        extra: Mapping[str, object] | None = None,
        wait_for_input: bool = False,
    ) -> None:
        super().critical(
            msg,
            *args,
            exc_info=exc_info,
            stack_info=stack_info,
            stacklevel=stacklevel,
            extra=extra,
        )
        if wait_for_input:
            self.wait_for_input()

    def exception(
        self,
        msg: object,
        *args: object,
        exc_info: (
            None
            | bool
            | tuple[type[BaseException], BaseException, TracebackType | None]
            | tuple[None, None, None]
            | BaseException
        ) = None,
        stack_info: bool = False,
        stacklevel: int = 1,
        extra: Mapping[str, object] | None = None,
        wait_for_input: bool = False,
    ) -> None:
        super().exception(
            msg,
            *args,
            exc_info=exc_info,
            stack_info=stack_info,
            stacklevel=stacklevel,
            extra=extra,
        )
        if wait_for_input:
            self.wait_for_input()

    def wait_for_input(self) -> None:
        """Wait for user input before continue"""
        input("[#] Press Enter to continue...")
