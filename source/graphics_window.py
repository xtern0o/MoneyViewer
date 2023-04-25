import random

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
matplotlib.use("Qt5Agg")

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QDate

from source.ui_generated_py_files.ui_graphics_window import Ui_Form
from source.payment_data import PaymentData
from source.db_class import Db


class MplCanvas1(FigureCanvas):
    def __init__(self, *args, **kwargs):
        self.fig = Figure()
        super(MplCanvas1, self).__init__(self.fig, *args, **kwargs)

    def plot(self, labels, men_means, women_means, x, width):
        self.fig.clear()

        self.ax = self.fig.add_subplot(111)

        rects1 = self.ax.bar(x - width / 2, men_means, width, label='Men')
        rects2 = self.ax.bar(x + width / 2, women_means, width, label='Women')
        self.ax.set_ylabel('Scores')
        self.ax.set_title('Scores by group and gender')
        self.ax.set_xticks(x)
        self.ax.set_xticklabels(labels)
        self.ax.legend()

        self.draw()


class GraphicsWindow(Ui_Form, QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.db = Db()
        self.setWindowTitle("Графический анализ расходов")

        self.canv1 = MplCanvas1()


        self.lay1.addWidget(self.canv1)
        # self.lay2.addWidget(self.canv2)

        self.current_date = QDate.currentDate()
        self.main_menu = parent

        self.date_1.setDate(QDate(self.current_date.year(), self.current_date.month(), 1))
        self.date_2.setDate(self.current_date)

        self.date_1.dateChanged.connect(self.build_canvas)
        self.date_2.dateChanged.connect(self.build_canvas)

        self.build_canvas()

    def build_canvas(self):
        self.error_lbl.setText("")
        date_left = self.date_1.date()
        date_right = self.date_2.date()
        if date_left > date_right:
            self.error_lbl.setText("Некорректные рамки даты")
            return
        payments = self.db.get_all_payments_from_this_user(self.main_menu.user_id)
        self.plot(payments)

    def plot(self, payments):
        data_1 = [1, 2, 3, 4, 5]
        data_2 = [1, 4, 2, 3, 1]

        payments_per_days = {}
        for payment in payments:
            if payment[-1] not in payments_per_days:
                payments_per_days[payment[-1]] = [payment]
            else:
                payments_per_days[payment[-1]].append(payment)
        print(payments_per_days)

        cats_per_day = {}
        for day in payments_per_days:
            for payment in payments_per_days[day]:
                if day not in cats_per_day:
                    cats_per_day[day] = {payment[3]: payment[4]}
                else:
                    cats_per_day[day][payment[3]] = cats_per_day[day].get(payment[3], 0) + payment[4]
        print(cats_per_day)

        cats_changing = {}
        # {1: [1045, 3299]}
        for day in cats_per_day:
            for cat in cats_per_day[day]:
                if cat not in cats_changing:
                    cats_changing[cat] = [cats_per_day[day][cat]]
                else:
                    cats_changing[cat].append(cats_per_day[day][cat])
        print(cats_changing)

        index1 = np.arange(len(cats_per_day))

        self.fig1.clear()
        ax1 = self.fig1.add_subplot(111)

        for day in cats_changing:
            for cat in cats_changing[day]:
                ax1.barh(index1, cat, color=self.db.get_category_by_id(cat)[-1])
        ax1.plot(data_1, '*-')
        self.canv1.draw()

        # self.fig2.clear()
        # ax2 = self.fig2.add_subplot(111)
        # ax2.plot(data_2, '*-')
        # self.canv2.draw()
