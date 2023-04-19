import datetime
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QSpacerItem
from PyQt5.QtCore import QDateTime

from source.ui_generated_py_files.ui_paymentdata import Ui_PaymentData
from source.filter_dialog import FilterDialog
from source.db_class import Db
from source.paymentdata_widget import PaymentDataWidget


class PaymentData(Ui_PaymentData, QWidget):
    def __init__(self, parent=None):
        super().__init__()

        self.db = Db()

        self.setupUi(self)
        self.setWindowTitle("Отображение расходов")

        self.main_menu = parent
        self.user_id = self.main_menu.user_id

        self.filter_settings = {"dt_borders": [],
                                "categories": []}

        self.filter_btn.clicked.connect(self.set_filter)

        self.refresh(**self.filter_settings)

    def set_filter(self):
        self.filter_dialog = FilterDialog(self)
        self.filter_dialog.show()

    def clear_widget_layout(self):
        if self.widgets_layout.count():
            for i in reversed(range(self.widgets_layout.count())):
                if self.widgets_layout.itemAt(i).widget():
                    self.widgets_layout.itemAt(i).widget().deleteLater()

    def fill_widget_layout(self):
        payments = self.db.get_all_payments_from_this_user(self.user_id)
        for payment in payments:
            w = PaymentDataWidget(payment[2], payment[5], payment[4], self.db.get_category_by_id(payment[3])[-1])
            self.widgets_layout.addWidget(w)
            print(w.name_lbl)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.widgets_layout.addItem(spacerItem1)

    def refresh(self, **kwargs):
        if kwargs["dt_borders"] and kwargs["categories"]:
            return
        self.clear_widget_layout()
        self.fill_widget_layout()


