# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btFlipH = QtWidgets.QPushButton(self.centralwidget)
        self.btFlipH.setObjectName("btFlipH")
        self.gridLayout.addWidget(self.btFlipH, 1, 0, 1, 1)
        self.btFlipV = QtWidgets.QPushButton(self.centralwidget)
        self.btFlipV.setObjectName("btFlipV")
        self.gridLayout.addWidget(self.btFlipV, 1, 1, 1, 1)
        self.btBlur = QtWidgets.QPushButton(self.centralwidget)
        self.btBlur.setObjectName("btBlur")
        self.gridLayout.addWidget(self.btBlur, 1, 2, 1, 1)
        self.btGrayscale = QtWidgets.QPushButton(self.centralwidget)
        self.btGrayscale.setObjectName("btGrayscale")
        self.gridLayout.addWidget(self.btGrayscale, 1, 3, 1, 1)
        self.lbImage = QtWidgets.QLabel(self.centralwidget)
        self.lbImage.setAlignment(QtCore.Qt.AlignCenter)
        self.lbImage.setObjectName("lbImage")
        self.gridLayout.addWidget(self.lbImage, 0, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFIles = QtWidgets.QMenu(self.menubar)
        self.menuFIles.setObjectName("menuFIles")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuOpen = QtWidgets.QAction(MainWindow)
        self.menuOpen.setObjectName("menuOpen")
        self.menuSave = QtWidgets.QAction(MainWindow)
        self.menuSave.setObjectName("menuSave")
        self.menuExit = QtWidgets.QAction(MainWindow)
        self.menuExit.setObjectName("menuExit")
        self.menuFIles.addAction(self.menuOpen)
        self.menuFIles.addAction(self.menuSave)
        self.menuFIles.addSeparator()
        self.menuFIles.addAction(self.menuExit)
        self.menubar.addAction(self.menuFIles.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btFlipH.setText(_translate("MainWindow", "Flip Horizontal"))
        self.btFlipV.setText(_translate("MainWindow", "Flip Vertical"))
        self.btBlur.setText(_translate("MainWindow", "Blur"))
        self.btGrayscale.setText(_translate("MainWindow", "Grayscale"))
        self.lbImage.setText(_translate("MainWindow", "No Image"))
        self.menuFIles.setTitle(_translate("MainWindow", "Files"))
        self.menuOpen.setText(_translate("MainWindow", "Open"))
        self.menuSave.setText(_translate("MainWindow", "Save"))
        self.menuExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

