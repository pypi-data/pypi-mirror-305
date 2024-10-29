from typing import Callable

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QPushButton, QCheckBox

from .widget import WidgetMix


class AbsButtonMix(WidgetMix):
    def __init__(self,
                 text: str = '', *,
                 icon: QIcon | str = None,
                 icon_size: int | tuple[int, int] = None,
                 checked=False,
                 checkable: bool = None,
                 auto_exclusive: bool = None,
                 on_toggled: Callable[[bool], None] = None,
                 **kwargs
                 ):
        super().__init__(**kwargs)
        if on_toggled: self.toggled.connect(on_toggled)
        if auto_exclusive is not None: self.setAutoExclusive(auto_exclusive)
        if checkable is not None: self.setCheckable(checkable)

        self.setText(text)
        self.setChecked(checked)

        if icon_size is not None:
            if isinstance(icon_size, int):
                icon_size = (icon_size, icon_size)
            self.setIconSize(*icon_size)
        if icon: self.setIcon(icon)

    def setIcon(self, icon: QIcon | QPixmap | str) -> None:
        icon = QIcon(icon) if isinstance(icon, str) else icon
        super().setIcon(icon)

    def setIconSize(self, w: int, h: int) -> None:
        super().setIconSize(QSize(w, h))


class Button(AbsButtonMix, QPushButton):
    def __init__(self, text='', *,
                 default: bool = None,
                 auto_default: bool = None,
                 appear='',
                 **kwargs
                 ):
        super().__init__(text, **kwargs)
        self.on_key_enter_pressed.connect(self.on_clicked.emit)
        if default is not None: self.setDefault(default)
        if auto_default is not None: self.setAutoDefault(auto_default)

        if appear == '':
            self.setStyleSheet(self.qss.merge({
                'background-color': ' #fff',
                'border': '1 solid #d1d1d1',
                'padding': '6 12',
                'border-radius': '4',
                ':hover': {
                    'background-color': '#f5f5f5',
                    'border': '1 solid #c7c7c7',
                    'border-radius': '4'
                },
                ':pressed': {
                    'background-color': '#e0e0e0',
                    'border': '1 solid #b3b3b3',
                },
            }))
        elif appear == 'subtle':
            self.setStyleSheet(self.qss.merge({
                'background-color': ' transparent',
                'border': '1 solid transparent',
                'padding': '6 12',
                'border-radius': '4',
                ':hover': {'background-color': '#f5f5f5'},
                ':pressed': {'background-color': '#e0e0e0'},
            }))


class SubtleButton(Button):
    def __init__(self, text='', **kwargs):
        super().__init__(text, appear='subtle', **kwargs)


class CheckBox(AbsButtonMix, QCheckBox):
    ...
