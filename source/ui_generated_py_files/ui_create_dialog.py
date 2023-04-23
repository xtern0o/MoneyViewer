# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_create_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(778, 272)
        Dialog.setStyleSheet("QDialog {\n"
"    background-color: #040c0e;\n"
"}\n"
"QFrame#frame, QFrame#frame_2, QFrame#frame_3 {\n"
"    background-color: #040c0e;\n"
"    border: 2px solid #be9063;\n"
"    border-radius: 20px;\n"
"}\n"
"QPushButton {\n"
"    font-family: Verdana, Geneva, sans-serif;\n"
"    font-size: 20px;\n"
"    letter-spacing: 2px;\n"
"    word-spacing: 6px;\n"
"    background-color: #132226;\n"
"    color: #a4978e;\n"
"    border-radius: 12px;\n"
"    outline:none\n"
"}\n"
"QPushButton#add_payment_btn:focus, QPushButton#add_category_btn:focus {\n"
"    background-color: #be9063;\n"
"    color: black;\n"
"    outline:none\n"
"}\n"
"QPushButton#essential_btn:checked {\n"
"    background-color: #be9063;\n"
"    color: #040c0e;\n"
"}\n"
"QPushButton:hover, QPushButton#essential_btn#focus {\n"
"    background-color: #525b56;\n"
"    color: #a4978e;\n"
"}\n"
"QLineEdit {\n"
"    background-color: #132226;\n"
"    color: #a4978e;\n"
"    border-radius: 12px;\n"
"    font-family: Verdana, Geneva, sans-serif;\n"
"    font-size: 20px;\n"
"    letter-spacing: 2px;\n"
"    word-spacing: 6px;\n"
"    opacity: 0.6;\n"
"    padding: 5px\n"
"}\n"
"QLineEdit:focus {\n"
"    background-color: #be9063;\n"
"    color: black;\n"
"    border-radius: 12px;\n"
"    font-family: Verdana, Geneva, sans-serif;\n"
"    font-size: 20px;\n"
"    letter-spacing: 2px;\n"
"    word-spacing: 6px;\n"
"    opacity: 0.6;\n"
"    padding: 5px\n"
"}\n"
"QLabel {\n"
"    font-family: Verdana, Geneva, sans-serif;\n"
"    font-size: 20px;\n"
"    letter-spacing: 2px;\n"
"    word-spacing: 6px;\n"
"    color: #525b56;\n"
"    background-color: #040c0e;\n"
"    border-radius: 10px;\n"
"}\n"
"QComboBox {\n"
"    background-color: #525b56;\n"
"    color: #a4978e;\n"
"    border-radius: 12px;\n"
"    font-family: Verdana, Geneva, sans-serif;\n"
"    font-size: 20px;\n"
"    letter-spacing: 2px;\n"
"    word-spacing: 6px;\n"
"    opacity: 0.6;\n"
"    padding: 10px\n"
"\n"
"}\n"
"QComboBox#focus {\n"
"    background-color: #be9063;\n"
"    color: black;\n"
"    border-radius: 12px;\n"
"    font-family: Verdana, Geneva, sans-serif;\n"
"    font-size: 20px;\n"
"    letter-spacing: 2px;\n"
"    word-spacing: 6px;\n"
"    opacity: 0.6;\n"
"    padding: 5px\n"
"}\n"
"QComboBox::drop-down {\n"
"    width: 40px;\n"
"    border: 0px;\n"
"/*    border-color: #525b56;*/\n"
"}\n"
"QComboBox::down-arrow {\n"
"    image: url(:/down-sign.png);\n"
"    width: 30px;\n"
"}\n"
"\n"
"QComboBox QListView {\n"
"    font-size: 12px;\n"
"    padding: 10px;\n"
"    outline: 0px;\n"
"    background-color: #040c0e;\n"
"    color: #a4978e;\n"
"    border-radius: 10px;\n"
"}\n"
"QComboBox QListView::item:hover {\n"
"    background-color: #be9063;\n"
"    color: black;\n"
"    border-radius: 5px;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setObjectName("stackedWidget")
        self.choice_page = QtWidgets.QWidget()
        self.choice_page.setObjectName("choice_page")
        self.gridLayout = QtWidgets.QGridLayout(self.choice_page)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 6, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.choice_page)
        self.label_6.setMinimumSize(QtCore.QSize(250, 30))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 5, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 2, 1, 1)
        self.frame = QtWidgets.QFrame(self.choice_page)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.add_payment_btn = QtWidgets.QPushButton(self.frame)
        self.add_payment_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.add_payment_btn.setIconSize(QtCore.QSize(40, 40))
        self.add_payment_btn.setObjectName("add_payment_btn")
        self.verticalLayout_2.addWidget(self.add_payment_btn)
        self.add_category_btn = QtWidgets.QPushButton(self.frame)
        self.add_category_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.add_category_btn.setIconSize(QtCore.QSize(40, 40))
        self.add_category_btn.setObjectName("add_category_btn")
        self.verticalLayout_2.addWidget(self.add_category_btn)
        self.gridLayout.addWidget(self.frame, 3, 0, 1, 3)
        self.stackedWidget.addWidget(self.choice_page)
        self.payment_page = QtWidgets.QWidget()
        self.payment_page.setObjectName("payment_page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.payment_page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.payment_page)
        self.label.setMinimumSize(QtCore.QSize(250, 30))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 3, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 4, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 3, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem7, 3, 2, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.payment_page)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.payment_le = QtWidgets.QLineEdit(self.frame_2)
        self.payment_le.setAlignment(QtCore.Qt.AlignCenter)
        self.payment_le.setClearButtonEnabled(True)
        self.payment_le.setObjectName("payment_le")
        self.gridLayout_3.addWidget(self.payment_le, 1, 0, 1, 1)
        self.category_cb = QtWidgets.QComboBox(self.frame_2)
        self.category_cb.setStyleSheet("")
        self.category_cb.setEditable(True)
        self.category_cb.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.category_cb.setDuplicatesEnabled(False)
        self.category_cb.setFrame(False)
        self.category_cb.setModelColumn(0)
        self.category_cb.setObjectName("category_cb")
        self.gridLayout_3.addWidget(self.category_cb, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.cost_le = QtWidgets.QLineEdit(self.frame_2)
        self.cost_le.setAlignment(QtCore.Qt.AlignCenter)
        self.cost_le.setClearButtonEnabled(True)
        self.cost_le.setObjectName("cost_le")
        self.gridLayout_3.addWidget(self.cost_le, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 2, 3)
        self.stackedWidget.addWidget(self.payment_page)
        self.category_page = QtWidgets.QWidget()
        self.category_page.setObjectName("category_page")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.category_page)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem8, 3, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem9, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.category_page)
        self.label_2.setMinimumSize(QtCore.QSize(250, 30))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 3, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem10, 4, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem11, 3, 2, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.category_page)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 4)
        self.color_btn = QtWidgets.QPushButton(self.frame_3)
        self.color_btn.setStyleSheet("border: 2px solid #be9063;")
        self.color_btn.setText("")
        self.color_btn.setObjectName("color_btn")
        self.gridLayout_5.addWidget(self.color_btn, 3, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem12, 3, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 3, 2, 1, 1)
        self.essential_btn = QtWidgets.QPushButton(self.frame_3)
        self.essential_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.essential_btn.setCheckable(True)
        self.essential_btn.setObjectName("essential_btn")
        self.gridLayout_5.addWidget(self.essential_btn, 2, 0, 1, 4)
        self.category_le = QtWidgets.QLineEdit(self.frame_3)
        self.category_le.setText("")
        self.category_le.setAlignment(QtCore.Qt.AlignCenter)
        self.category_le.setObjectName("category_le")
        self.gridLayout_5.addWidget(self.category_le, 1, 0, 1, 4)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem13, 3, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame_3, 1, 0, 1, 3)
        self.stackedWidget.addWidget(self.category_page)
        self.verticalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_6.setText(_translate("Dialog", "[↑] [↓] [Tab] [Enter]"))
        self.label_5.setText(_translate("Dialog", "Новый(-ая)"))
        self.add_payment_btn.setText(_translate("Dialog", "Расход"))
        self.add_category_btn.setText(_translate("Dialog", "Категория"))
        self.label.setText(_translate("Dialog", "[Ctrl + Q]"))
        self.payment_le.setText(_translate("Dialog", "название"))
        self.label_4.setText(_translate("Dialog", "Новый расход"))
        self.cost_le.setText(_translate("Dialog", "цена"))
        self.label_2.setText(_translate("Dialog", "Подтвердить [Ctrl + Q]"))
        self.label_3.setText(_translate("Dialog", "Новая категория расходов"))
        self.label_7.setText(_translate("Dialog", "Цвет [Shift + W]"))
        self.essential_btn.setText(_translate("Dialog", "обязательный расход? [Shift + E]"))
