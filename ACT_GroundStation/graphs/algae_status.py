
from tkinter import font
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget




class algae_status(QWidget):
    
    def __init__(self):    
        super().__init__()
        self.isEjected = False

        vbox = QVBoxLayout()
        titleLabel = QLabel("Algae Status")
        titleLabel.setAlignment(Qt.AlignCenter)
        self.setLabelFont(titleLabel, 30, color=(255,255,255))

        self.statusLabel = QLabel("Ejection Ready")
        self.statusLabel.setAlignment(Qt.AlignHCenter)
        self.setLabelFont(self.statusLabel, 40, color=(92,209,229), bold=True)
        
        vbox.addWidget(titleLabel)
        vbox.addSpacing(10)
        vbox.addWidget(self.statusLabel)
        self.setLayout(vbox)

        self.setStyleSheet("background-color: rgb(60,60,60)")


    def setLabelFont(self, label:QLabel, size:int, color:tuple, bold=False):
        label.setFont(self.customFont(size, bold))
        pal = label.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor(color[0],color[1],color[2]))
        label.setPalette(pal)


    def customFont(self, fontsize, bold=False):
        font = QtGui.QFont()
        font.setPixelSize(fontsize)
        font.setBold(bold)
        return font
        

    def update(self, isEject):
        if(self.isEjected == False and int(isEject)):
            self.statusLabel.setText("Ejected")
            self.setLabelFont(self.statusLabel, 40, color=(255,0,40), bold=True)
            self.isEjected = True



"""

class algae_status(pg.PlotWidget):
    
    def __init__(self, font = None):    
        super().__init__()
        self.setTitle("Algae Status", color='w', size="18pt")

        self.getPlotItem().hideAxis('bottom')
        self.getPlotItem().hideAxis('left')


        #self.Ejected = pg.TextItem("Ejected",color=(255,0,127), anchor=(0.5,0.5))
        self.EjectReady = pg.TextItem(" ",color=(92,209,229), anchor=(0.5, 0.5))
        #self.Ejected.setFont(font)
        self.EjectReady.setFont(font)
        

        self.addItem(self.EjectReady)
        

    def update(self, isEjection):
        if(isEjection):

            self.EjectReady.setText("Ejection Ready")
            #self.EjectReady.updateTextPos()
        else:
            self.EjectReady.setText("Ejected")


"""

