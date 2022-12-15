import sys

from PyQt5.QtWidgets import QApplication
from source.reg_window import RegWindow


def except_hook(c, e, t):
    sys.__excepthook__(c, e, t)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = RegWindow()
    win.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
