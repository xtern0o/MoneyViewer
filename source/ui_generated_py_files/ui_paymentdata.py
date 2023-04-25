# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_paymentdata.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PaymentData(object):
    def setupUi(self, PaymentData):
        PaymentData.setObjectName("PaymentData")
        PaymentData.resize(844, 472)
        PaymentData.setStyleSheet("QWidget#PaymentData {\n"
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
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(PaymentData)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(PaymentData)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filter_btn = QtWidgets.QPushButton(self.frame_2)
        self.filter_btn.setMinimumSize(QtCore.QSize(150, 40))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/filter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.filter_btn.setIcon(icon)
        self.filter_btn.setIconSize(QtCore.QSize(30, 30))
        self.filter_btn.setObjectName("filter_btn")
        self.horizontalLayout.addWidget(self.filter_btn)
        spacerItem = QtWidgets.QSpacerItem(374, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.sum_lbl = QtWidgets.QLabel(self.frame_2)
        self.sum_lbl.setObjectName("sum_lbl")
        self.horizontalLayout.addWidget(self.sum_lbl)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.docx_btn = QtWidgets.QPushButton(self.frame_2)
        self.docx_btn.setMinimumSize(QtCore.QSize(100, 40))
        self.docx_btn.setText("")
        self.docx_btn.setObjectName("docx_btn")
        self.horizontalLayout.addWidget(self.docx_btn)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(PaymentData)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 796, 342))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widgets_layout = QtWidgets.QVBoxLayout()
        self.widgets_layout.setObjectName("widgets_layout")
        self.gridLayout_2.addLayout(self.widgets_layout, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(PaymentData)
        QtCore.QMetaObject.connectSlotsByName(PaymentData)

    def retranslateUi(self, PaymentData):
        _translate = QtCore.QCoreApplication.translate
        PaymentData.setWindowTitle(_translate("PaymentData", "Form"))
        self.filter_btn.setText(_translate("PaymentData", " Filter"))
        self.sum_lbl.setText(_translate("PaymentData", "Сумма: 32731"))
