import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtWidgets, QtCore
from src.ui.mainwindow import Ui_MainWindow

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.redAdd.clicked.connect(self.redAddClick)
        self.ui.blueAdd.clicked.connect(self.blueAddClick)
        self.ui.scoreClear.clicked.connect(self.scoreClearClick)
        self.redScore=0
        self.blueScore=0
        self.fileWrite()
        self.show()

    def __del__(self):
        self.redTxt.close()
        self.blueTxt.close()

    def fileWrite(self):
        self.redTxt=open("./redScore.txt","w")
        self.redTxt.write(str(self.redScore))
        self.blueTxt=open("./blueScore.txt","w")
        self.blueTxt.write(str(self.blueScore))
        self.redTxt.close()
        self.blueTxt.close()

    def redAddClick(self):
        self.redScore+=1
        self.ui.radScore.display(self.redScore)
        self.fileWrite()

    def blueAddClick(self):
        self.blueScore+=1
        self.ui.blueScore.display(self.blueScore)
        self.fileWrite()

    def scoreClearClick(self):
        self.redScore=0
        self.blueScore=0
        self.ui.blueScore.display(self.blueScore)
        self.ui.radScore.display(self.redScore)
        self.fileWrite()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
