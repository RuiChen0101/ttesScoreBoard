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
        self.ui.redAddRound.clicked.connect(self.redAddRoundClick)
        self.ui.blueAdd.clicked.connect(self.blueAddClick)
        self.ui.blueAddRound.clicked.connect(self.blueAddRoundClick)
        self.ui.scoreClear.clicked.connect(self.scoreClearClick)
        self.ui.roundClear.clicked.connect(self.roundClearClick)
        self.redScore=0
        self.redRoundScore=0
        self.redRoundScoreTxt="○○"
        self.blueScore=0
        self.blueRoundScore=0
        self.blueRoundScoreTxt="○○"
        self.roundSet=2
        self.fileWrite()
        self.show()

    def fileWrite(self):
        open("./redScore.txt","w",encoding="utf-8").write(str(self.redScore))
        open("./blueScore.txt","w",encoding="utf-8").write(str(self.blueScore))
        open("./redRound.txt","w",encoding="utf-8").write(str(self.redRoundScoreTxt))
        open("./blueRound.txt","w",encoding="utf-8").write(str(self.blueRoundScoreTxt))

    def redAddClick(self):
        self.redScore+=1
        self.ui.radScore.display(self.redScore)
        self.fileWrite()

    def blueAddClick(self):
        self.blueScore+=1
        self.ui.blueScore.display(self.blueScore)
        self.fileWrite()

    def redAddRoundClick(self):
        self.redRoundScore+=1 if self.redRoundScore<self.roundSet else 0
        self.redRoundScoreTxt=""
        for _ in range(0,self.redRoundScore):
            self.redRoundScoreTxt+="●"
        for _ in range(self.redRoundScore,self.roundSet):
            self.redRoundScoreTxt+="○"
        self.scoreClearClick()

    def blueAddRoundClick(self):
        self.blueRoundScore+=1 if self.blueRoundScore<self.roundSet else 0
        self.blueRoundScoreTxt=""
        for _ in range(0,self.blueRoundScore):
            self.blueRoundScoreTxt+="●"
        for _ in range(self.blueRoundScore,self.roundSet):
            self.blueRoundScoreTxt+="○"
        self.scoreClearClick()

    def scoreClearClick(self):
        self.redScore=0
        self.blueScore=0
        self.ui.blueScore.display(self.blueScore)
        self.ui.radScore.display(self.redScore)
        self.ui.redRound.setText(self.redRoundScoreTxt)
        self.ui.blueRound.setText(self.blueRoundScoreTxt)
        self.fileWrite()

    def roundClearClick(self):
        self.roundSet=int(self.ui.roundSet.toPlainText()) if int(self.ui.roundSet.toPlainText())>=2 else 2
        self.redScore=0
        self.redRoundScore=0
        self.redRoundScoreTxt=""
        for _ in range(0,self.roundSet):
            self.redRoundScoreTxt+="○"
        self.blueScore=0
        self.blueRoundScore=0
        self.blueRoundScoreTxt=""
        for _ in range(0,self.roundSet):
            self.blueRoundScoreTxt+="○"
        self.ui.blueScore.display(self.blueScore)
        self.ui.radScore.display(self.redScore)
        self.ui.redRound.setText(self.redRoundScoreTxt)
        self.ui.blueRound.setText(self.blueRoundScoreTxt)
        self.fileWrite()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
