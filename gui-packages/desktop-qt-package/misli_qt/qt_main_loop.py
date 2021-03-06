from typing import Callable
from PySide2.QtCore import QTimer
from misli.main_loop import MainLoop


class QtMainLoop(MainLoop):
    def call_delayed(
            self,
            callback: Callable,
            delay: float = 0,
            args: list = None,
            kwargs: dict = None):

        args = args or []
        kwargs = kwargs or {}
        QTimer.singleShot(delay * 1000, lambda: callback(*args, **kwargs))
