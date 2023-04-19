from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui
from PyQt5.QtCore import QDate

from source.ui_generated_py_files.ui_payment_widget import Ui_PaymentDataWidget


class PaymentDataWidget(Ui_PaymentDataWidget, QWidget):
    def __init__(self, name, date, cost, color, parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent

        self.name_lbl.setText(name)
        self.cost_lbl.setText(str(cost))
        self.date_lbl.setText(date)
        self.frame.setStyleSheet("""
        QFrame#frame{{border: 2px solid {}}}
        """.format(color))

        self.settings_btn.clicked.connect(self.open_settings)

    def open_settings(self):
        # TODO: widget_settings
        pass

    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:
        # TODO: widget_settings
        pass