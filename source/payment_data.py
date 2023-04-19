import datetime
from PyQt5.QtWidgets import QWidget
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

    def refresh(self, **kwargs):
        payments = self.db.get_all_payments_from_this_user(self.main_menu.user_id)
        if kwargs["dt_borders"] and kwargs["categories"]:
            pass
        for payment in payments:
            pw = PaymentDataWidget(payment[3], payment[4], payment[5])
        print(payments)
