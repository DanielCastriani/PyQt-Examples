# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maindesigner.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(272, 241)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.leInputText = QtWidgets.QLineEdit(self.centralwidget)
        self.leInputText.setObjectName("leInputText")
        self.verticalLayout.addWidget(self.leInputText)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.btApply = QtWidgets.QPushButton(self.centralwidget)
        self.btApply.setObjectName("btApply")
        self.verticalLayout.addWidget(self.btApply)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btApply.clicked.connect(self.onClick_Apply)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main"))
        self.label.setText(_translate("MainWindow", "No Clicks"))
        self.btApply.setText(_translate("MainWindow", "Apply"))

    def onClick_Apply(self):
        text = self.leInputText.text()
        print(text)
        self.label.setText(text)
        self.leInputText.setFocus()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

