from PyQt5.QtWidgets import QDialog, QCheckBox
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QKeyEvent

from source.ui_generated_py_files.ui_filter_window import Ui_FilterDialog
from source.db_class import Db
from source.other_stylesheets import CHECK_BOX_STYLESHEET


class FilterDialog(Ui_FilterDialog, QDialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.scrollArea.verticalScrollBar().setStyleSheet("""
        
QScrollBar:vertical
    {
        background-color: #be9063;
        width: 20px;
        margin: 15px 3px 15px 3px;
        border-radius: 3px;
    }

QScrollBar::handle:vertical
    {
        background-color: #d5be45;
        min-height: 5px;
        border-radius: 4px;
    }
        """)
        self.scrollArea.verticalScrollBar().setVisible(False)

        self.dt_2.setDate(QDate.currentDate())

        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.payment_data_window = parent
        self.user_id = self.payment_data_window.user_id
        self.db = Db()

        self.categories_from_custom_choice = []

        self.init_categories()

        self.radioButton.clicked.connect(self.change_btn_choice)
        self.essential_rb.clicked.connect(self.change_btn_choice)
        self.notessential_rb.clicked.connect(self.change_btn_choice)
        self.other_groups_rb.clicked.connect(self.change_btn_choice)

    def init_categories(self):
        for category in self.db.get_categories_from_this_user(self.user_id):
            btn = QCheckBox(self)
            btn.setText(str(category[1]))
            btn.setStyleSheet(CHECK_BOX_STYLESHEET)
            btn.setChecked(True)
            self.categories_from_custom_choice.append(btn)
            self.bittons_layout.addWidget(btn)

    def keyPressEvent(self, event: QKeyEvent):
        if int(event.modifiers()) == Qt.ControlModifier:
            if event.key() == Qt.Key_Q:
                date1 = self.dt_1.date()
                date2 = self.dt_2.date()
                selected_cats = [cat.text() for cat in list(filter(lambda btn: btn.isChecked(),
                                                                   self.categories_from_custom_choice))]
                self.payment_data_window.refresh(dt_borders=(date1, date2), categories=selected_cats)
                self.close()
        if event.key() == Qt.Key_Escape:
            self.close()

    def change_btn_choice(self):
        name = self.sender().text()
        if name == "Все":
            self.off_every_btn()
            for btn in self.categories_from_custom_choice:
                btn.setChecked(True)
        elif name == "Обязательные":
            self.off_every_btn()
            essential = [cat[1] for cat in list(filter(lambda n: n[2], self.db.get_categories_from_this_user(self.user_id)))]
            for btn in self.categories_from_custom_choice:
                if btn.text() in essential:
                    btn.setChecked(True)
        elif name == "Необязательные":
            self.off_every_btn()
            notessential = [cat[1] for cat in list(filter(lambda n: not n[2], self.db.get_categories_from_this_user(self.user_id)))]
            for btn in self.categories_from_custom_choice:
                if btn.text() in notessential:
                    btn.setChecked(True)
        elif name == "Другие":
            self.off_every_btn()

    def off_every_btn(self):
        for btn in self.categories_from_custom_choice:
            btn.setChecked(False)
