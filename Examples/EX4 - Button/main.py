import sys
from PyQt5 import QtWidgets


class Win(QtWidgets.QWidget):
    _count = 0
    def __init__(self):
        super().__init__()
        self.resize(300,150)
        self.init_components()   

    def init_components(self):
        self.btInc = QtWidgets.QPushButton('PushButton')
        self.lbCount = QtWidgets.QLabel('Count:' + str(self._count))
        gridLayout = QtWidgets.QGridLayout()
        gridLayout.addWidget(self.btInc,0,0,1,-1)
        gridLayout.addWidget(self.lbCount,1,1,1,1)
        self.setLayout(gridLayout)
        self.setWindowTitle("Ex4")
        
        self.btInc.clicked.connect(self.btInc_clicked)
    

    def btInc_clicked(self):
        self._count += 1
        self.lbCount.setText('Clicked:' + str(self._count))


application = QtWidgets.QApplication(sys.argv)
w = Win()
w.show()
sys.exit(application.exec_())
