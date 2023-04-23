from PyQt5.QtWidgets import QMainWindow
from source.ui_generated_py_files.ui_mainmenu import Ui_MainMenu

from source.db_class import Db
from source.create_dialog import CreateDialog
from source.payment_data import PaymentData
from source.category_editor import CategoryEditor
from source.graphics_window import GraphicsWindow


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
        self.payments_btn.clicked.connect(self.open_paymentdata)
        self.settings_btn.clicked.connect(self.open_category_editor)
        self.graphs_btn.clicked.connect(self.open_graphs)

    def logout(self):
        self.db.set_remembered(self.user_id, False)
        self.close()

    def create_dialog_foo(self):
        self.create_dialog = CreateDialog(self.user_id, self)
        self.create_dialog.show()

    def open_paymentdata(self):
        self.paymentdata = PaymentData(self)
        self.paymentdata.show()

    def open_category_editor(self):
        self.cat_editor = CategoryEditor(self)
        self.cat_editor.show()

    def open_graphs(self):
        self.gr = GraphicsWindow(self)
        self.gr.show()

