from PyQt5.QtWidgets import QMainWindow

from source.ui_generated_py_files.ui_reg_window import Ui_RegWindow
from source.main_menu import MainMenu
from source.db_class import Db


def password_small_validation(pwd: str) -> bool:
    return len(pwd) >= 4


def login_small_validation(login: str) -> bool:
    return len(login) > 3


class RegWindow(Ui_RegWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = Db()

        self.setupUi(self)
        self.statusbar.setStyleSheet("color: pink")

        self.check_remember()

        self.reg_btn.clicked.connect(self.reg)
        self.login_btn.clicked.connect(self.login)

    def check_remember(self):
        data = self.db.find_remembered_user()
        if data:
            self.main_menu = MainMenu(data[0], self)
            self.main_menu.show()
            self.close()
        self.last_user_id = data[0] if data else None

    def login(self):
        user_id = self.db.get_userid_if_correct_pwd(self.login_le.text(), self.password_le.text())
        if user_id:
            if self.last_user_id:
                self.db.set_remembered(self.last_user_id, False)
            self.db.set_remembered(user_id, self.remember_btn.isChecked())

            self.main_menu = MainMenu(user_id, self)
            self.main_menu.show()
            self.close()
        else:
            self.statusbar.showMessage("[!] Неправильный логин и/или пароль")

    def reg(self):
        if self.db.does_exists_user_with_this_username(self.login_le.text()):
            self.statusbar.showMessage("[!] Пользователь с таким именем уже существует", 2500)
        else:
            if login_small_validation(self.login_le.text()) and password_small_validation(self.password_le.text()):
                self.db.add_user(self.login_le.text(), self.password_le.text(), self.remember_btn.isChecked())
                self.statusbar.showMessage("[0] Пользователь с именем {}"
                                           " Успешно зарегистрирован".format(self.login_le.text()), 2500)
            else:
                self.statusbar.showMessage("[!] Длина пароля должна быть больше либо равна 4, а логина - больше 3")