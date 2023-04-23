from PyQt5.QtWidgets import QWidget, QSpacerItem, QSizePolicy

from source.ui_generated_py_files.ui_category_editor import Ui_Form
from source.db_class import Db
from source.category_widget import CategoryWidget


class CategoryEditor(Ui_Form, QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        self.db = Db()
        self.main_menu = parent

        self.save_btn.clicked.connect(self.save)
        self.cancel_btn.clicked.connect(self.close)

        self.load_categories()

    def load_categories(self):
        categories = self.db.get_categories_from_this_user(self.main_menu.user_id)
        for cat in categories:
            self.verticalLayout_2.addWidget(CategoryWidget(cat[1], cat[2], cat[3], cat[0]))
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)

    def refresh_categories(self):
        if self.verticalLayout_2.count():
            for i in reversed(range(self.verticalLayout_2.count())):
                if self.verticalLayout_2.itemAt(i).widget():
                    self.verticalLayout_2.itemAt(i).widget().deleteLater()
        self.load_categories()

    def save(self):
        for i in range(self.verticalLayout_2.count()):
            w: CategoryWidget = self.verticalLayout_2.itemAt(i).widget()
            if not isinstance(w, QSpacerItem) and w:
                if w.delete_btn.isChecked():
                    self.db.delete_category(w.id)
                else:
                    self.db.update_category(w.id, w.name.text(), w.color, w.essential_btn.isChecked())
        self.refresh_categories()
        self.save_btn.setStyleSheet(f"""
        QPushButton#save_btn:hover {{
            background-color: rgba(59, 200, 34, 200);
            color: black;
        }}
        """)