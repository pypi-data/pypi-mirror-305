from PySide6.QtGui import QFont
from PySide6.QtGui import QFontDatabase


class FontDatabase(QFontDatabase):
    @classmethod
    def applicationFontFamilies(cls, fileNames: list[str]) -> list[str]:
        return [super().applicationFontFamilies(y) for
                y in [cls.addApplicationFont(x) for x in fileNames]]


class Font(QFont):
    def __init__(self,
                 families='Segoe UI, Microsoft YaHei, PingFang SC', *,
                 size=13,
                 weight=QFont.Weight.Normal,
                 italic=False,
                 ):
        super().__init__([x.strip() for x in families.split(',')], -1, weight, italic)
        self.setPixelSize(size)
