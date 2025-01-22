# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main_page(object):
    def setupUi(self, Main_page):
        Main_page.setObjectName("Main_page")
        Main_page.resize(540, 428)
        Main_page.setStyleSheet("background-color: #ffffff;")
        self.centralwidget = QtWidgets.QWidget(Main_page)
        self.centralwidget.setObjectName("centralwidget")
        self.leave = QtWidgets.QPushButton(self.centralwidget)
        self.leave.setGeometry(QtCore.QRect(120, 390, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.leave.setFont(font)
        self.leave.setStyleSheet("QPushButton {\n"
"    background-color: #4CAF50;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 5px 15px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #367c39;\n"
"}")
        self.leave.setObjectName("leave")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 390, 81, 31))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: #4CAF50;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 5px 15px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #367c39;\n"
"}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 511, 35))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_note = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_note.setFont(font)
        self.btn_note.setStyleSheet("QPushButton {\n"
"    background-color: #4CAF50;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 5px 15px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #367c39;\n"
"}")
        self.btn_note.setObjectName("btn_note")
        self.horizontalLayout.addWidget(self.btn_note)
        self.note_inf = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.note_inf.setFont(font)
        self.note_inf.setStyleSheet("QPushButton {\n"
"    background-color: #4CAF50;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 5px 15px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #367c39;\n"
"}")
        self.note_inf.setObjectName("note_inf")
        self.horizontalLayout.addWidget(self.note_inf)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 90, 511, 35))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_book = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_book.setFont(font)
        self.btn_book.setStyleSheet("QPushButton {\n"
"    background-color: #4CAF50;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 5px 15px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #367c39;\n"
"}")
        self.btn_book.setObjectName("btn_book")
        self.horizontalLayout_2.addWidget(self.btn_book)
        self.book_inf = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.book_inf.setFont(font)
        self.book_inf.setStyleSheet("QPushButton {\n"
"    background-color: #4CAF50;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 5px 15px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #367c39;\n"
"}")
        self.book_inf.setObjectName("book_inf")
        self.horizontalLayout_2.addWidget(self.book_inf)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 140, 511, 35))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dishes_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dishes_btn.setFont(font)
        self.dishes_btn.setStyleSheet("QPushButton {\n"
"    background-color: #4CAF50;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 5px 15px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #367c39;\n"
"}")
        self.dishes_btn.setObjectName("dishes_btn")
        self.horizontalLayout_3.addWidget(self.dishes_btn)
        self.dishes_inf_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dishes_inf_btn.setFont(font)
        self.dishes_inf_btn.setStyleSheet("QPushButton {\n"
"    background-color: #4CAF50;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 5px 15px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #45a049;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #367c39;\n"
"}")
        self.dishes_inf_btn.setObjectName("dishes_inf_btn")
        self.horizontalLayout_3.addWidget(self.dishes_inf_btn)
        Main_page.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main_page)
        QtCore.QMetaObject.connectSlotsByName(Main_page)

    def retranslateUi(self, Main_page):
        _translate = QtCore.QCoreApplication.translate
        Main_page.setWindowTitle(_translate("Main_page", "Головна сторінка"))
        self.leave.setText(_translate("Main_page", "Повернутись до привітання"))
        self.btn_note.setText(_translate("Main_page", "Нотатки для здоров\'я"))
        self.note_inf.setText(_translate("Main_page", "Як користуватись"))
        self.btn_book.setText(_translate("Main_page", "Довідник"))
        self.book_inf.setText(_translate("Main_page", "Як користуватись"))
        self.dishes_btn.setText(_translate("Main_page", "Старовинні страви"))
        self.dishes_inf_btn.setText(_translate("Main_page", "Як користуватись"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main_page = QtWidgets.QMainWindow()
    ui = Ui_Main_page()
    ui.setupUi(Main_page)
    Main_page.show()
    sys.exit(app.exec_())
