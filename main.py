import sys
from source.db_class import Db

from PyQt5.QtWidgets import QApplication

from source.main_menu import MainMenu
from source.reg_window import RegWindow


def except_hook(c, e, t):
    sys.__excepthook__(c, e, t)


if __name__ == "__main__":
    db = Db()
    db.create_db()
    app = QApplication(sys.argv)
    if user := db.find_remembered_user():
        main_menu = MainMenu(user[0])
        main_menu.show()
    else:
        win = RegWindow()
        win.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
