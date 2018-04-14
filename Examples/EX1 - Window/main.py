import sys
from PyQt5 import QtWidgets

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    w.setWindowTitle("PyQt5")
    # x,y,w,h
    w.setGeometry(100,300,300,500)
    w.show()
    sys.exit(app.exec_())

window()