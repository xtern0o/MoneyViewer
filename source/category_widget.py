from PyQt5.QtWidgets import QWidget, QColorDialog

from source.ui_generated_py_files.ui_category_widget import Ui_Form


class CategoryWidget(Ui_Form, QWidget):
    def __init__(self, name: str, essential: bool, color: str, category_id: int):
        super().__init__()
        self.setupUi(self)

        self.color = color
        self.id = category_id
        self.name.setText(name)
        self.essential_btn.setChecked(essential)
        self.color_frame.setStyleSheet(f"""
QFrame#color_frame {{
    border: 2px solid {self.color};
    border-radius: 20px;
}}
        """)

        self.color_btn.clicked.connect(self.choose_color)

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color = color.name()
            self.color_frame.setStyleSheet(f"""
            QPushButton#color_btn:hover {{
                background-color: {color.name()};
            }}
            """)