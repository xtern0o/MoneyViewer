# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_graphics_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1067, 648)
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Form.setStyleSheet("QWidget#Form {\n"
"    background-color: #040c0e;\n"
"}\n"
"QFrame#frame, QFrame#frame_2 {\n"
"    background-color: #040c0e;\n"
"    border: 2px solid #be9063;\n"
"    border-radius: 20px;\n"
"}\n"
"QDateTimeEdit {\n"
"    font-family: Verdana, Geneva, sans-serif;\n"
"    font-size: 20px;\n"
"    letter-spacing: 2px;\n"
"    word-spacing: 6px;\n"
"    background-color: #132226;\n"
"    color: #a4978e;\n"
"    border-radius: 12px;\n"
"    padding: 3px;\n"
"}\n"
"QLabel {\n"
"    font-family: Verdana, Geneva, sans-serif;\n"
"    font-size: 20px;\n"
"    letter-spacing: 2px;\n"
"    word-spacing: 6px;\n"
"    color: #be9063;\n"
"}\n"
"QLabel#label_3 {\n"
"    font-family: Verdana, Geneva, sans-serif;\n"
"    font-size: 20px;\n"
"    letter-spacing: 2px;\n"
"    word-spacing: 6px;\n"
"    color: #be9063;\n"
"    background-color: #040c0e;\n"
"    border-radius: 15px;\n"
"}\n"
"QRadioButton {\n"
"    font-family: Verdana, Geneva, sans-serif;\n"
"    font-size: 20px;\n"
"    letter-spacing: 2px;\n"
"    word-spacing: 6px;\n"
"    color: #a4978e;\n"
"}\n"
"QRadioButton:checked {\n"
"    color: #be9063;\n"
"    font: 75 20pt \"Verdana\";\n"
"    text-decoration: underline;\n"
"}\n"
"QRadioButton::indicator {\n"
"    background-color: #132226;\n"
"    border-radius: 5px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #be9063;\n"
"}\n"
"\n"
"QScrollArea {\n"
"    background-color: #132226;\n"
"    border-radius: 15px;\n"
"    padding: 10px;\n"
"}\n"
"QWidget#scrollAreaWidgetContents {\n"
"    background-color: #132226;\n"
"    border: 0px;\n"
"}\n"
"QPushButton {\n"
"    font-family: Verdana, Geneva, sans-serif;\n"
"    font-size: 20px;\n"
"    letter-spacing: 2px;\n"
"    word-spacing: 6px;\n"
"    background-color: #132226;\n"
"    color: #a4978e;\n"
"    border-radius: 12px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #525b56;\n"
"    color: #a4978e;\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: #be9063;\n"
"    color: #040c0e;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.title = QtWidgets.QLabel(Form)
        self.title.setMaximumSize(QtCore.QSize(16777215, 50))
        self.title.setStyleSheet("font-size: 40px;\n"
"")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.date_1 = QtWidgets.QDateEdit(self.frame)
        self.date_1.setObjectName("date_1")
        self.horizontalLayout.addWidget(self.date_1)
        self.date_2 = QtWidgets.QDateEdit(self.frame)
        self.date_2.setObjectName("date_2")
        self.horizontalLayout.addWidget(self.date_2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 3)
        self.graph_1 = QtWidgets.QWidget(self.frame)
        self.graph_1.setMinimumSize(QtCore.QSize(500, 400))
        self.graph_1.setStyleSheet("border: 2px solid #be9063;\n"
"border-radius: 10px;")
        self.graph_1.setObjectName("graph_1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.graph_1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lay1 = QtWidgets.QVBoxLayout()
        self.lay1.setObjectName("lay1")
        self.verticalLayout.addLayout(self.lay1)
        self.gridLayout_2.addWidget(self.graph_1, 5, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setStyleSheet("    color: #a4978e;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 4, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 3)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(230, 0))
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 4, 2, 1, 1)
        self.graph_2 = QtWidgets.QWidget(self.frame)
        self.graph_2.setMinimumSize(QtCore.QSize(500, 400))
        self.graph_2.setStyleSheet("border: 2px solid #be9063;\n"
"border-radius: 10px;")
        self.graph_2.setObjectName("graph_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.graph_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lay2 = QtWidgets.QVBoxLayout()
        self.lay2.setObjectName("lay2")
        self.verticalLayout_2.addLayout(self.lay2)
        self.gridLayout_2.addWidget(self.graph_2, 5, 1, 1, 2)
        self.error_lbl = QtWidgets.QLabel(self.frame)
        self.error_lbl.setStyleSheet("color: pink;")
        self.error_lbl.setText("")
        self.error_lbl.setObjectName("error_lbl")
        self.gridLayout_2.addWidget(self.error_lbl, 6, 0, 1, 3)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title.setText(_translate("Form", "Графический анализ"))
        self.label.setText(_translate("Form", "Расходы в течение времени"))
        self.label_4.setText(_translate("Form", "до..."))
        self.label_3.setText(_translate("Form", "начиная с.."))
        self.label_2.setText(_translate("Form", "Отношение категорий"))
        self.pushButton.setText(_translate("Form", "по обязательности"))
