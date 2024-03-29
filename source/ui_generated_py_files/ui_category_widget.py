# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_category_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(864, 97)
        Form.setStyleSheet("QWidget#Form {\n"
"    background-color: #040c0e;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-family: Verdana, Geneva, sans-serif;\n"
"    font-size: 20px;\n"
"    letter-spacing: 2px;\n"
"    word-spacing: 6px;\n"
"    color: #a4978e;\n"
"}\n"
"QLabel:hover {\n"
"    color: #F3E0D2;\n"
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
"QLineEdit {\n"
"    background-color: #525b56;\n"
"    color: #a4978e;\n"
"    border-radius: 12px;\n"
"    font-family: Verdana, Geneva, sans-serif;\n"
"    font-size: 20px;\n"
"    letter-spacing: 2px;\n"
"    word-spacing: 6px;\n"
"    opacity: 0.6;\n"
"    padding: 5px\n"
"}\n"
"QFrame#frame, QFrame#frame_2 {\n"
"    background-color: #040c0e;\n"
"    border: 2px solid #be9063;\n"
"    border-radius: 20px;\n"
"}\n"
"QLabel#login_label, QLabel#password_label {\n"
"    font-family: Verdana, Geneva, sans-serif;\n"
"    font-size: 30px;\n"
"    letter-spacing: 2px;\n"
"    word-spacing: 6px;\n"
"    color: #525b56;\n"
"}\n"
"QPushButton#remember_btn:checked {\n"
"    background-color: #be9063;\n"
"    color: #040c0e;\n"
"}\n"
"QPushButton#add_btn:hover {\n"
"    background-color: rgba(59, 200, 34, 200);\n"
"}\n"
"QWidget#scrollAreaWidgetContents {\n"
"    background-color: #040c0e;\n"
"}\n"
"QScrollArea {\n"
"    border-color: #040c0e;\n"
"}\n"
"QPushButton#essential_btn:checked {\n"
"    background-color: #be9063;\n"
"    color: #040c0e;\n"
"}\n"
"QPushButton#delete_btn:checked {\n"
"    background-color: red;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.color_frame = QtWidgets.QFrame(Form)
        self.color_frame.setMaximumSize(QtCore.QSize(16777215, 60))
        self.color_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.color_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.color_frame.setObjectName("color_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.color_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.name = QtWidgets.QLineEdit(self.color_frame)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 0, 0, 1, 1)
        self.color_btn = QtWidgets.QPushButton(self.color_frame)
        self.color_btn.setMinimumSize(QtCore.QSize(80, 40))
        self.color_btn.setObjectName("color_btn")
        self.gridLayout.addWidget(self.color_btn, 0, 2, 1, 1)
        self.essential_btn = QtWidgets.QPushButton(self.color_frame)
        self.essential_btn.setMinimumSize(QtCore.QSize(280, 40))
        self.essential_btn.setCheckable(True)
        self.essential_btn.setChecked(False)
        self.essential_btn.setDefault(False)
        self.essential_btn.setFlat(False)
        self.essential_btn.setObjectName("essential_btn")
        self.gridLayout.addWidget(self.essential_btn, 0, 1, 1, 1)
        self.delete_btn = QtWidgets.QPushButton(self.color_frame)
        self.delete_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.delete_btn.setMaximumSize(QtCore.QSize(40, 40))
        self.delete_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_btn.setIcon(icon)
        self.delete_btn.setIconSize(QtCore.QSize(30, 30))
        self.delete_btn.setCheckable(True)
        self.delete_btn.setChecked(False)
        self.delete_btn.setObjectName("delete_btn")
        self.gridLayout.addWidget(self.delete_btn, 0, 3, 1, 1)
        self.verticalLayout.addWidget(self.color_frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.name.setText(_translate("Form", "название"))
        self.color_btn.setText(_translate("Form", "цвет"))
        self.essential_btn.setText(_translate("Form", "обязательный расход"))
