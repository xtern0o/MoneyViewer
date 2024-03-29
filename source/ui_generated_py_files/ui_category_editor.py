# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_category_editor.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(847, 520)
        Form.setStyleSheet("QWidget#Form {\n"
"    background-color: #040c0e;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-family: Verdana, Geneva, sans-serif;\n"
"    font-size: 40px;\n"
"    letter-spacing: 2px;\n"
"    word-spacing: 6px;\n"
"    color: #be9063;\n"
"}\n"
"QLabel:hover {\n"
"    font-size: 40px;\n"
"    letter-spacing: 2px;\n"
"    word-spacing: 6px;\n"
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
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.save_btn = QtWidgets.QPushButton(self.frame)
        self.save_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.save_btn.setObjectName("save_btn")
        self.gridLayout.addWidget(self.save_btn, 3, 1, 1, 1)
        self.cancel_btn = QtWidgets.QPushButton(self.frame)
        self.cancel_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.cancel_btn.setObjectName("cancel_btn")
        self.gridLayout.addWidget(self.cancel_btn, 3, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_2)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 773, 354))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 2)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Редактор категорий"))
        self.save_btn.setText(_translate("Form", "Сохранить"))
        self.cancel_btn.setText(_translate("Form", "Отмена"))
        self.label.setText(_translate("Form", "Редактор категорий"))
