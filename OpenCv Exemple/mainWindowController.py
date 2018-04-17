from PyQt5 import QtWidgets
from PyQt5.QtGui import QImage,QPixmap
from UI.mainWindow import Ui_MainWindow
import numpy as np
import cv2
import sys
import imghdr


class MainWindowController(object):
    def __init__(self):
        self.image = None
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.__setup()  

    def __setup(self):
        self.ui.menuOpen.setShortcut("Ctrl+O")
        self.ui.menuOpen.setToolTip("Open an image")
        self.ui.menuOpen.triggered.connect(self.onTriggerd_menuOpen)
        self.ui.menuSave.setShortcut("Ctrl+S")
        self.ui.menuSave.setToolTip("Save image")
        self.ui.menuSave.triggered.connect(self.onTriggerd_menuSave)
        self.ui.menuExit.triggered.connect(self.exit_app)
        self.ui.btFlipH.clicked.connect(self.filtH)
        self.ui.btFlipV.clicked.connect(self.filtV)
        self.ui.btBlur.clicked.connect(self.blur)
        self.ui.btGrayscale.clicked.connect(self.grayscale)

    def onTriggerd_menuOpen(self):        
        dialog = QtWidgets.QFileDialog()        
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode())        
        file = dialog.getOpenFileName(None,'Open an image')
        if file and len(file[0]) > 0:
            filePath = file[0]
            isImage = imghdr.what(filePath)           
            print("File Infos:",len(file))
            print("path: ",filePath)
            print("Type: ",file[1])            
            if isImage is not None:
                self.image = cv2.imread(filePath,cv2.IMREAD_UNCHANGED)
                if self.image is None:
                    print("Error")
                else:
                    self.show_image()
            else:
                print("isn't an image")     
        else:
            print("Open a file")

    def show_image(self):
        size = self.image.shape
        step = self.image.size / size[0]
        if len(size) == 3:
            if size[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        else:                    
            qformat = QImage.Format_Indexed8
        img = QImage(self.image, size[1], size[0], step, qformat)
        img = img.rgbSwapped()
        pixMap = QPixmap.fromImage(img)
        self.ui.lbImage.setPixmap(pixMap)

    def onTriggerd_menuSave(self):
        if self.image is not None:
            dialog = QtWidgets.QFileDialog()        
            dialog.setFileMode(QtWidgets.QFileDialog.FileMode())        
            file = dialog.getSaveFileName(None,'Save an image')
            if file and len(file[0]) > 0:
                cv2.imwrite(file[0] +".png",self.image)
        else:
            print("Open an image")

    def exit_app(self):
        sys.exit()

    def filtH(self):  
        if self.image is not None:      
            self.image = cv2.flip(self.image,0)
            self.show_image()

    def filtV(self):  
        if self.image is not None:    
            self.image = cv2.flip(self.image,1)
            self.show_image()

    def grayscale(self):            
        if self.image is not None:    
            self.image = cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY) 
            self.show_image()

    def blur(self):        
        if self.image is not None:
            self.image = cv2.blur(self.image,(5,5))
            self.show_image()

if __name__ == "__main__":
    ctr = MainWindowController()
    ctr.MainWindow.show()
    sys.exit(ctr.app.exec_())  