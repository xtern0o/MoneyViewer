from PyQt5.QtWidgets import QMainWindow

from source.db_class import Db
from ui_generated_py_files.ui_mainmenu import Ui_MainMenu


class MainMenu(Ui_MainMenu, QMainWindow):
    def __init__(self, user_id, parent=None):
        super().__init__()
        self.db = Db()
        self.setupUi(self)
        self.user_id = user_id
        self.parent = parent
