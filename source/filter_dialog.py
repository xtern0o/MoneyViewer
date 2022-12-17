from PyQt5.QtWidgets import QDialog, QButtonGroup, QCheckBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent

from source.ui_generated_py_files.ui_filter_window import Ui_FilterDialog
from source.db_class import Db
from source.other_stylesheets import CHECK_BOX_STYLESHEET


class FilterDialog(Ui_FilterDialog, QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.payment_data_window = parent
        self.user_id = self.payment_data_window.user_id
        self.db = Db()

        self.cat_bgroup = QButtonGroup(self)

    def init_categories(self):
        self.cat_list.setVisible(False)
        for category in self.db.get_exist_categories():
            btn = QCheckBox(self)
            btn.setText(category)
            btn.setStyleSheet(CHECK_BOX_STYLESHEET)
            self.cat_bgroup.addButton(btn)
            self.bittons_layout.addWidget(btn)

    def keyPressEvent(self, event: QKeyEvent):
        if int(event.modifiers()) == Qt.ControlModifier:
            if event.key() == Qt.Key_Q:
                # TODO: фильтр
                args = []
                self.payment_data_window.refresh(args)
        if event.key() == Qt.Key_Escape:
            self.close()