# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/ui/mainui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(286, 321)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.redAdd = QtWidgets.QPushButton(self.centralwidget)
        self.redAdd.setGeometry(QtCore.QRect(30, 200, 93, 28))
        self.redAdd.setObjectName("redAdd")
        self.blueAdd = QtWidgets.QPushButton(self.centralwidget)
        self.blueAdd.setGeometry(QtCore.QRect(170, 200, 93, 28))
        self.blueAdd.setObjectName("blueAdd")
        self.scoreClear = QtWidgets.QPushButton(self.centralwidget)
        self.scoreClear.setGeometry(QtCore.QRect(100, 270, 93, 28))
        self.scoreClear.setObjectName("scoreClear")
        self.radScore = QtWidgets.QLCDNumber(self.centralwidget)
        self.radScore.setGeometry(QtCore.QRect(40, 40, 71, 91))
        self.radScore.setDigitCount(1)
        self.radScore.setProperty("intValue", 0)
        self.radScore.setObjectName("radScore")
        self.blueScore = QtWidgets.QLCDNumber(self.centralwidget)
        self.blueScore.setGeometry(QtCore.QRect(180, 40, 61, 91))
        self.blueScore.setDigitCount(1)
        self.blueScore.setProperty("intValue", 0)
        self.blueScore.setObjectName("blueScore")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 47, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 20, 47, 12))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.redAdd.setText(_translate("MainWindow", "紅隊加分"))
        self.blueAdd.setText(_translate("MainWindow", "藍隊加分"))
        self.scoreClear.setText(_translate("MainWindow", "清除分數"))
        self.label.setText(_translate("MainWindow", "紅隊分數"))
        self.label_2.setText(_translate("MainWindow", "藍隊分數"))
