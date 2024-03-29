# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_payment_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PaymentDataWidget(object):
    def setupUi(self, PaymentDataWidget):
        PaymentDataWidget.setObjectName("PaymentDataWidget")
        PaymentDataWidget.resize(800, 100)
        PaymentDataWidget.setMinimumSize(QtCore.QSize(800, 100))
        PaymentDataWidget.setMaximumSize(QtCore.QSize(16777215, 100))
        PaymentDataWidget.setStyleSheet("QWidget#PaymentDataWidget {\n"
"    background-color: #040c0e;\n"
"}\n"
"QFrame#frame, QFrame#frame_2 {\n"
"    background-color: #040c0e;\n"
"    border: 2px solid #be9063;\n"
"    border-radius: 20px;\n"
"}\n"
"QWidget#scrollAreaWidgetContents {\n"
"    background-color: #040c0e;\n"
"}\n"
"QScrollArea {\n"
"    border-color: #040c0e;\n"
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
"QLabel {\n"
"    font-family: Verdana, Geneva, sans-serif;\n"
"    font-size: 20px;\n"
"    letter-spacing: 2px;\n"
"    word-spacing: 6px;\n"
"    color: #be9063;\n"
"}\n"
"QLabel:hover {\n"
"    letter-spacing: 2px;\n"
"    word-spacing: 6px;\n"
"    color: #F3E0D2;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(PaymentDataWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(PaymentDataWidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.name_lbl = QtWidgets.QLabel(self.frame)
        self.name_lbl.setMinimumSize(QtCore.QSize(300, 0))
        self.name_lbl.setMaximumSize(QtCore.QSize(16777215, 50))
        self.name_lbl.setStyleSheet("font-size: 30px;")
        self.name_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.name_lbl.setObjectName("name_lbl")
        self.gridLayout.addWidget(self.name_lbl, 0, 0, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 2, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 2, 1)
        self.settings_btn = QtWidgets.QPushButton(self.frame)
        self.settings_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.settings_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        self.settings_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_btn.setIcon(icon)
        self.settings_btn.setIconSize(QtCore.QSize(30, 30))
        self.settings_btn.setObjectName("settings_btn")
        self.gridLayout.addWidget(self.settings_btn, 0, 7, 1, 1)
        self.date_lbl = QtWidgets.QLabel(self.frame)
        self.date_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.date_lbl.setObjectName("date_lbl")
        self.gridLayout.addWidget(self.date_lbl, 0, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(46, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 5, 2, 1)
        self.cost_lbl = QtWidgets.QLabel(self.frame)
        self.cost_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.cost_lbl.setObjectName("cost_lbl")
        self.gridLayout.addWidget(self.cost_lbl, 1, 4, 1, 1)
        self.label_money_ico = QtWidgets.QLabel(self.frame)
        self.label_money_ico.setAlignment(QtCore.Qt.AlignCenter)
        self.label_money_ico.setObjectName("label_money_ico")
        self.gridLayout.addWidget(self.label_money_ico, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(PaymentDataWidget)
        QtCore.QMetaObject.connectSlotsByName(PaymentDataWidget)

    def retranslateUi(self, PaymentDataWidget):
        _translate = QtCore.QCoreApplication.translate
        PaymentDataWidget.setWindowTitle(_translate("PaymentDataWidget", "Form"))
        self.name_lbl.setText(_translate("PaymentDataWidget", "gdfgfdf"))
        self.date_lbl.setText(_translate("PaymentDataWidget", "22.08.1921"))
        self.cost_lbl.setText(_translate("PaymentDataWidget", "23344"))
        self.label_money_ico.setText(_translate("PaymentDataWidget", "$"))
        self.label.setText(_translate("PaymentDataWidget", "*"))
