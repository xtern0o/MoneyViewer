# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_filter_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FilterDialog(object):
    def setupUi(self, FilterDialog):
        FilterDialog.setObjectName("FilterDialog")
        FilterDialog.resize(686, 527)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        FilterDialog.setFont(font)
        FilterDialog.setStyleSheet("QDialog {\n"
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
"    color: #a4978e;\n"
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
"}")
        self.gridLayout = QtWidgets.QGridLayout(FilterDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(FilterDialog)
        self.label_3.setMinimumSize(QtCore.QSize(0, 30))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(FilterDialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.frame)
        self.dateTimeEdit_2.setMinimumSize(QtCore.QSize(0, 40))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.gridLayout_2.addWidget(self.dateTimeEdit_2, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.choice_rb_group = QtWidgets.QButtonGroup(FilterDialog)
        self.choice_rb_group.setObjectName("choice_rb_group")
        self.choice_rb_group.addButton(self.radioButton)
        self.horizontalLayout.addWidget(self.radioButton)
        self.essential_rb = QtWidgets.QRadioButton(self.frame)
        self.essential_rb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.essential_rb.setAutoFillBackground(False)
        self.essential_rb.setChecked(False)
        self.essential_rb.setObjectName("essential_rb")
        self.choice_rb_group.addButton(self.essential_rb)
        self.horizontalLayout.addWidget(self.essential_rb)
        self.notessential_rb = QtWidgets.QRadioButton(self.frame)
        self.notessential_rb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.notessential_rb.setAutoFillBackground(False)
        self.notessential_rb.setObjectName("notessential_rb")
        self.choice_rb_group.addButton(self.notessential_rb)
        self.horizontalLayout.addWidget(self.notessential_rb)
        self.other_groups_rb = QtWidgets.QRadioButton(self.frame)
        self.other_groups_rb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.other_groups_rb.setAutoFillBackground(False)
        self.other_groups_rb.setObjectName("other_groups_rb")
        self.choice_rb_group.addButton(self.other_groups_rb)
        self.horizontalLayout.addWidget(self.other_groups_rb)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 2)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.frame)
        self.dateTimeEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout_2.addWidget(self.dateTimeEdit, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 618, 245))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.bittons_layout = QtWidgets.QVBoxLayout()
        self.bittons_layout.setObjectName("bittons_layout")
        self.verticalLayout_2.addLayout(self.bittons_layout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 4, 0, 1, 2)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(FilterDialog)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.retranslateUi(FilterDialog)
        QtCore.QMetaObject.connectSlotsByName(FilterDialog)

    def retranslateUi(self, FilterDialog):
        _translate = QtCore.QCoreApplication.translate
        FilterDialog.setWindowTitle(_translate("FilterDialog", "Dialog"))
        self.label_3.setText(_translate("FilterDialog", "Filter"))
        self.radioButton.setText(_translate("FilterDialog", "Все"))
        self.essential_rb.setText(_translate("FilterDialog", "Обязательные"))
        self.notessential_rb.setText(_translate("FilterDialog", "Необязательные"))
        self.other_groups_rb.setText(_translate("FilterDialog", "Другие"))
        self.label_4.setText(_translate("FilterDialog", "Показать категории..."))
        self.label.setText(_translate("FilterDialog", "Показать расходы с..."))
        self.label_2.setText(_translate("FilterDialog", "до..."))
        self.label_5.setText(_translate("FilterDialog", "apply: [Ctrl + Q]"))
