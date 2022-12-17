import datetime
from PyQt5.QtWidgets import QWidget

from source.ui_generated_py_files.ui_paymentdata import Ui_PaymentData
from source.filter_dialog import FilterDialog


class PaymentData(Ui_PaymentData, QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Отображение расходов")

        self.main_menu = parent
        self.user_id = self.main_menu.user_id

        self.filter_settings = {"dt_borders": [],
                                "categories": []}

        self.filter_btn.clicked.connect(self.set_filter)

    def set_filter(self):
        self.filter_dialog = FilterDialog(self)
        self.filter_dialog.show()

    def refresh(self, **kwargs):
        # TODO: ререшер фильтр
        print(kwargs)

