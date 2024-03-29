import datetime as dt
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QColorDialog

from source.ui_generated_py_files.ui_create_dialog import Ui_Dialog
from source.db_class import Db
from source.other_stylesheets import ERROR_LABEL_STYLESHEET


class CreateDialog(Ui_Dialog, QDialog):
    def __init__(self, user_id, parent=None):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.main_menu = parent
        self.user_id = user_id

        self.db = Db()

        self.stackedWidget.setCurrentIndex(0)

        self.category_cb.addItems(list(map(lambda n: n[1], self.db.get_categories_from_this_user(self.main_menu.user_id))))

        self.add_payment_btn.clicked.connect(self.goto_new_payment)
        self.add_category_btn.clicked.connect(self.goto_new_category)

        self.color_btn.clicked.connect(self.get_color)
        self.color = "#be9063"

    def goto_new_payment(self):
        self.stackedWidget.setCurrentIndex(1)
        self.payment_le.setFocus()

    def goto_new_category(self):
        self.stackedWidget.setCurrentIndex(2)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            self.close()
        if event.key() == Qt.Key_Minus:
            self.stackedWidget.setCurrentIndex(0)

        if self.stackedWidget.currentIndex() == 1:
            if int(event.modifiers()) == Qt.ControlModifier:
                if event.key() == Qt.Key_Q:
                    name = self.payment_le.text()
                    category = self.category_cb.currentText()
                    cost = self.cost_le.text()
                    current_dt = str(dt.date.today())
                    if self.is_valid_new_payment_data(cost) and self.is_valid_category(category) and name != "название":
                        if self.db.add_new_payment(self.user_id, name, category, cost, current_dt):
                            self.close()
                        else:
                            self.label_4.setText("Категории не существует")
                            self.label_4.setStyleSheet(ERROR_LABEL_STYLESHEET)
                    else:
                        self.label_4.setText("Некорректный ввод")
                        self.label_4.setStyleSheet(ERROR_LABEL_STYLESHEET)
            if event.key() == Qt.Key_Escape:
                self.close()

        elif self.stackedWidget.currentIndex() == 2:
            if int(event.modifiers()) == Qt.ShiftModifier:
                if event.key() == Qt.Key_W:
                    self.get_color()
            if int(event.modifiers()) == Qt.ControlModifier:
                if event.key() == Qt.Key_Q:
                    name = self.category_le.text()
                    essential = self.essential_btn.isChecked()
                    color = self.color
                    if self.is_valid_category(name):
                        self.db.add_new_category(name, essential, color, self.main_menu.user_id)
                        self.close()
            if int(event.modifiers()) == Qt.ShiftModifier:
                if event.key() == Qt.Key_E:
                    self.essential_btn.setChecked(not self.essential_btn.isChecked())
            if event.key() == Qt.Key_Escape:
                self.close()

    def is_valid_new_payment_data(self, cost):
        try:
            if int(cost):
                return True
            return False
        except Exception:
            return False

    def is_valid_category(self, cat_name):
        return cat_name != "" and cat_name != "категория"

    def get_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color_btn.setStyleSheet("""
            border: 2px solid {};
            """.format(color.name()))
            self.frame_3.setStyleSheet("""
            QFrame#frame_3 {{
                border: 2px solid {}
            }}
            """.format(color.name()))
            self.color = color.name()
            print(self.color)

