from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent

from source.ui_generated_py_files.ui_create_dialog import Ui_Dialog


class CreateDialog(Ui_Dialog, QDialog):
    def __init__(self, user_id, parent=None):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.main_menu = parent
        self.user_id = user_id

        self.stackedWidget.setCurrentIndex(0)

        self.add_payment_btn.clicked.connect(self.goto_new_payment)
        self.add_category_btn.clicked.connect(self.goto_new_category)

    def goto_new_payment(self):
        self.stackedWidget.setCurrentIndex(1)

    def goto_new_category(self):
        self.stackedWidget.setCurrentIndex(2)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            self.close()
        if event.key() == Qt.Key_Minus:
            self.stackedWidget.setCurrentIndex(0)

        if self.stackedWidget.currentIndex() == 1:
            if int(event.modifiers()) == Qt.ControlModifier:
                if event.key() == Qt.Key_Space:
                    print("db add payment and check valid")

        elif self.stackedWidget.currentIndex() == 2:
            if int(event.modifiers()) == Qt.ControlModifier:
                if event.key() == Qt.Key_Space:
                    print("db add category and check valid")
            if int(event.modifiers()) == Qt.ShiftModifier:
                if event.key() == Qt.Key_E:
                    self.essential_btn.setChecked(not self.essential_btn.isChecked())

