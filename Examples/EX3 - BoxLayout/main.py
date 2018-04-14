import sys
from PyQt5 import QtWidgets

def window():
    count = 0
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()

    hBox = QtWidgets.QHBoxLayout()
    vBox = QtWidgets.QVBoxLayout()    
    
    bt = QtWidgets.QPushButton('Click')
    lbCount = QtWidgets.QLabel('Click Count:' + str(count))

    vBox.addWidget(bt) 
    
    hBox.addStretch()
    hBox.addWidget(lbCount)
    hBox.addStretch()

    w.setLayout(vBox)
    vBox.addLayout(hBox)   

    w.setWindowTitle('PyQt5')
    w.show()
    sys.exit(app.exec_())

window()