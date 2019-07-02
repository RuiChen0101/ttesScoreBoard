import sys
import os
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtWidgets, QtCore
from src.ui.mainwindow import Ui_MainWindow

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.redAdd.clicked.connect(self.redAddClick)
        self.ui.redAdd_2.clicked.connect(self.redAddClick_2)
        self.ui.blueAdd.clicked.connect(self.blueAddClick)
        self.ui.blueAdd_2.clicked.connect(self.blueAddClick_2)
        self.ui.scoreClear.clicked.connect(self.scoreClearClick)
        self.redScore=0
        self.redBigScore=0
        self.redBigScoreTxt="○○"
        self.blueScore=0
        self.blueBigScore=0
        self.blueBigScoreTxt="○○"
        self.roundSet=2
        self.fileWrite()
        self.show()

    def fileWrite(self):
        open("./redScore.txt","w",encoding="utf-8").write(str(self.redScore))
        open("./blueScore.txt","w",encoding="utf-8").write(str(self.blueScore))
        open("./redRound.txt","w",encoding="utf-8").write(str(self.redBigScoreTxt))
        open("./blueRound.txt","w",encoding="utf-8").write(str(self.blueBigScoreTxt))

    def redAddClick(self):
        self.redScore+=1
        self.ui.radScore.display(self.redScore)
        self.fileWrite()

    def blueAddClick(self):
        self.blueScore+=1
        self.ui.blueScore.display(self.blueScore)
        self.fileWrite()

    def redAddClick_2(self):
        self.redBigScore+=1 if self.redBigScore<self.roundSet else 0
        self.redBigScoreTxt=""
        for _ in range(0,self.redBigScore):
            self.redBigScoreTxt+="●"
        for _ in range(self.redBigScore,self.roundSet):
            self.redBigScoreTxt+="○"
        self.ui.redBig.setText(self.redBigScoreTxt)
        self.fileWrite()

    def blueAddClick_2(self):
        self.blueBigScore+=1 if self.blueBigScore<self.roundSet else 0
        self.blueBigScoreTxt=""
        for _ in range(0,self.blueBigScore):
            self.blueBigScoreTxt+="●"
        for _ in range(self.blueBigScore,self.roundSet):
            self.blueBigScoreTxt+="○"
        self.ui.blueBig.setText(self.blueBigScoreTxt)
        self.fileWrite()

    def scoreClearClick(self):
        self.roundSet=int(self.ui.roundSet.toPlainText()) if int(self.ui.roundSet.toPlainText())>=2 else 2
        self.redScore=0
        self.redBigScore=0
        self.redBigScoreTxt=""
        for _ in range(0,self.roundSet):
            self.redBigScoreTxt+="○"
        self.blueScore=0
        self.blueBigScore=0
        self.blueBigScoreTxt=""
        for _ in range(0,self.roundSet):
            self.blueBigScoreTxt+="○"
        self.ui.blueScore.display(self.blueScore)
        self.ui.radScore.display(self.redScore)
        self.ui.redBig.setText(self.redBigScoreTxt)
        self.ui.blueBig.setText(self.blueBigScoreTxt)
        self.fileWrite()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
