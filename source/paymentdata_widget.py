from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui
from PyQt5.QtCore import QDate

from source.ui_generated_py_files.ui_payment_widget import Ui_PaymentDataWidget


class PaymentDataWidget(Ui_PaymentDataWidget, QWidget):
    def __init__(self, name, date, cost, parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent

        self.name_lbl = name
        self.date_lbl = date
        self.cost_lbl = str(cost)

        self.settings_btn.clicked.connect(self.open_settings)

    def open_settings(self):
        # TODO: widget_settings
        pass

    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:
        # TODO: widget_settings
        pass