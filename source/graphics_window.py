from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QDate

from source.ui_generated_py_files.ui_graphics_window import Ui_Form


class GraphicsWindow(Ui_Form, QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        self.current_date = QDate.currentDate()

        self.date_1.setDate(QDate(self.current_date.year(), self.current_date.month(), 1))
        self.date_2.setDate(self.current_date)

