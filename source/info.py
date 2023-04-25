from source.ui_generated_py_files.ui_info import Ui_Form
from source.db_class import Db

from PyQt5.QtWidgets import QWidget


class InfoWindow(Ui_Form, QWidget):
    def __init__(self, payments, parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent

        self.payments = payments

        self.db = Db()
        self.fil_set = self.parent.filter_settings

        if self.payments:
            payments_per_days = {}
            for payment in self.payments:
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

            cats_sum = {}
            for cat in cats_changing:
                cats_sum[cat] = sum(cats_changing[cat])

            ess = {"1": 0, "0": 0}
            for cat in cats_sum:
                if self.db.get_category_by_id(cat)[2]:
                    ess["1"] += cats_sum[cat]
                else:
                    ess["0"] += cats_sum[cat]

            self.max_lbl.setText(str(sum(list(map(lambda n: n[4], self.payments)))))
            self.max_cat_lbl.setText(self.db.get_category_by_id(max(cats_sum, key=lambda n: cats_sum[n]))[1])
            if ess["0"] != 0:
                n = ess['1'] / ess['0']
                self.ess_to_lbl.setText(str(f"{n:.2}"))
                if n >= 3:
                    self.mark_frame.setStyleSheet("""
                    background-color: #408e29;
                    border-radius: 5px;
                    """)
                elif 1 < n < 3:
                    self.mark_frame.setStyleSheet("""
                    background-color: #b7d31a;
                    border-radius: 5px;
                    """)
                else:
                    self.mark_frame.setStyleSheet("""
                    background-color: #c90d0d;
                    border-radius: 5px;
                    """)

            cost_per_days = {}
            for day in cats_per_day:
                for cat in cats_per_day[day]:
                    cost_per_days[day] = cost_per_days.get(day, 0) + cats_per_day[day][cat]

            self.max_date.setText(max(cost_per_days, key=lambda n: cost_per_days[n]))
            self.cost_max_date.setText(str(cost_per_days[max(cost_per_days, key=lambda n: cost_per_days[n])]))
