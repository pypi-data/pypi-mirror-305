from typing import Callable

from PySide6.QtWidgets import QDialog

from .widget import WidgetMix, QLayout


class Dialog(WidgetMix, QDialog):
    def __init__(self, layout: QLayout = None,
                 accepted: Callable = None,
                 rejected: Callable = None,
                 finished: Callable[[int], None] = None,
                 **kwargs
                 ):
        super().__init__(layout=layout, **kwargs)
        if accepted: self.accepted.connect(accepted)
        if rejected: self.rejected.connect(rejected)
        if finished: self.finished.connect(finished)
