import sys
from PyQt5 import QtWidgets, QtGui

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()    
    w.setGeometry(150,150,400,400)

    lbTxt = QtWidgets.QLabel(w)    
    lbImg = QtWidgets.QLabel(w)

    lbTxt.setText('Hello')


    #add image
    qpmImg = QtGui.QPixmap('./Examples/EX2 - label, image/qt.png')
    lbImg.setPixmap(qpmImg)


    #x,y
    lbTxt.move(20,20)
    lbImg.move(20,35)

    w.setWindowTitle('Label Examples')
    w.show()
    sys.exit(app.exec_())

window()