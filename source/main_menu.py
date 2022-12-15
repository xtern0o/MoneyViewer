from PyQt5.QtWidgets import QMainWindow

from source.db_class import Db
from source.ui_generated_py_files.ui_mainmenu import Ui_MainMenu
from source.create_dialog import CreateDialog


class MainMenu(Ui_MainMenu, QMainWindow):
    def __init__(self, user_id, parent=None):
        super().__init__()
        self.db = Db()
        self.setupUi(self)
        self.user_id = user_id
        self.reg_window = parent

        self.username_lbl.setText(self.db.get_username(self.user_id))

        self.exit_btn.clicked.connect(self.logout)
        self.add_btn.clicked.connect(self.create_dialog_foo)

    def logout(self):
        self.db.set_remembered(self.user_id, False)
        self.reg_window.login_le.setText("")
        self.reg_window.password_le.setText("")
        self.reg_window.remember_btn.setChecked(False)
        self.close()

    def create_dialog_foo(self):
        self.create_dialog = CreateDialog(self.user_id, self)
        self.create_dialog.show()

