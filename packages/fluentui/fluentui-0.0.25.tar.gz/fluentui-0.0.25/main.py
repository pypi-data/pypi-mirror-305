from PySide6.QtWidgets import QDialog

from src.fluentui.widgets import Application, Widget

if __name__ == '__main__':
    print('---------------------')
    app = Application()

    w = Widget()
    edit = QDialog(w)

    print(w.children())
    print(edit.parentWidget())

    w.show()
    app.exec()
