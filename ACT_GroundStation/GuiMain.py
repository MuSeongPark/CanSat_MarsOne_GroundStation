
import sys, time
from threading import Timer
from tkinter import font
#from matplotlib.pyplot import title

import pyqtgraph as pg
from pyqtgraph import PlotWidget
from pyqtgraph.Qt import QtCore, QtWidgets
from SerialCommunication import Communication

from PyQt5.QtWidgets import *

"""
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QMainWindow,
QLabel, QLineEdit, QTextEdit, QVBoxLayout, QHBoxLayout)
"""

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from pyqtgraph.Qt import QtGui

#import graphs
from graphs.graph_dioxid import graph_dioxid
from graphs.graph_acceleration import graph_acceleration
from graphs.graph_altitude import graph_altitude
from graphs.algae_status import algae_status

#import other functions
from function.MapLayout import MapLayout
from function.CameraLayout import CameraLayout
from function.CameraThread import ThreadClass
from DataBase import DataBase


"""
#Caution!
 1.) You must turn on your Cansat power first!
 2.) And then, connect a Xbee Port in this GUI

#Data Table
[Date, CO2, Acceleration, latitude, longitude, Altitude, Eject]

"""



#latitude=35.15688919999978
#longitude=128.09505469999976

latitude=34.610619
longitude=127.208198

zoom=18


class GroundStationUI(QWidget):
    def __init__(self):
        super().__init__()
        self.comboBox = QComboBox()
        self.connect_btn = QPushButton('Connect')
        self.dataBase = DataBase()

        self.com = Communication(9600, self.comboBox, self.connect_btn)
        self.initUI()
        time.sleep(1)

        ###
        #self.camThread = ThreadClass()


    def initUI(self):
        #pyqt graph area style
        pg.setConfigOption('background', (60,60,60))
        pg.setConfigOption('foreground', (255,255,255))
       
        hbox1 = QHBoxLayout()#button, combobox
        hbox2 = QHBoxLayout()#map + vbox1
        hbox3 = QHBoxLayout()#CO2, Altitude, MPU, Data

        vbox1 = QVBoxLayout()#배터리 전압, 씨앗 사출
        mainLayout = QVBoxLayout()#외곽 vbox


        title_label = QLabel('Cansat Ground Station')
        title_label.setAlignment(Qt.AlignCenter)
        self.setLabelFont(title_label, 60, True)

        self.mapbox = MapLayout(latitude, longitude, zoom)
        
        #graph layout
        dioxid_layout = self.setDioxidGraph()
        altitude_layout =self.setAltitudeGraph()
        acc_layout = self.setAccelGraph()
        camera_layout= self.setCamera()
        algae_widget = self.setAlgaeStatus()

        #data button & combobox Layout
        hbox1.addLayout(self.button_layout(),2)
        hbox1.addSpacing(20)
        hbox1.addStretch(3)
        hbox1.addLayout(self.combobox_layout(),1)
        
        #battery & algae Layout
        vbox1.addLayout(camera_layout,4)
        #vbox1.addWidget(camera_layout, 4)
        vbox1.addSpacing(10)
        vbox1.addWidget(algae_widget,1)

        #vbox1 & map Layout
        hbox2.addLayout(vbox1, 1)
        hbox2.addSpacing(10)
        hbox2.addLayout(self.mapbox, 2)

        #add the other graphs to Layout
        hbox3.addLayout(dioxid_layout,1)
        hbox3.addSpacing(10)
        hbox3.addLayout(altitude_layout,1)
        hbox3.addSpacing(10)
        hbox3.addLayout(acc_layout,1)

        mainLayout.addWidget(title_label)
        mainLayout.addLayout(hbox1)
        mainLayout.addSpacing(20)
        mainLayout.addLayout(hbox2,2)

        #Add CO2, Altitude, Acceleration Graph Layout
        mainLayout.addSpacing(10)
        mainLayout.addLayout(hbox3,1)

        mainLayout.setContentsMargins(40,20,40,40) #left, top, right, bottom
        self.setLayout(mainLayout)
        

        
        self.setStyleSheet("background-color: rgb(50,50,50)")

        self.setWindowIcon(QIcon("icon.png"))
        self.setWindowTitle('Cansat Ground Station')
        self.setGeometry(40,60,1850,1100)
        self.show()


    def setCamera(self):
        """
        example
        widg = pq.PlotWidget(background=(0, 0, 0, 255), x=[0, 1, 2, 3], 
                             y=[0, 1, 2, 3],font= font,font_size= 30)
        """

        #카메라 수정부분
        #camera = CameraLayout()
        self.camera = CameraLayout()

        return self.camera

    def setAlgaeStatus(self):
        self.algae = algae_status()
        
        #w = PlotWidget()
        #w.setTitle("Algae Status", color='w', size="18pt")

        hbox = QHBoxLayout()
        widget = QWidget()

        hbox.addWidget(self.algae)
        widget.setLayout(hbox)
        widget.setStyleSheet("background-color: rgb(60,60,60)")

        return widget

    def setAltitudeGraph(self):
        #get altitude graph here
        self.altitude = graph_altitude()

        hbox = QHBoxLayout()
        hbox.addWidget(self.altitude)
        return hbox

    def setDioxidGraph(self):
        #get dioxid graph here
        self.dioxid = graph_dioxid()

        hbox = QHBoxLayout()
        hbox.addWidget(self.dioxid)
        return hbox

    def setAccelGraph(self):
        #get acceleration graph here
        self.acc = graph_acceleration()

        hbox = QHBoxLayout()
        hbox.addWidget(self.acc)
        return hbox
        
    def button_layout(self):
        #button style
        style = "background-color:rgb(25,215,76);color:rgb(0,0,0);font-size:24px;"
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        label = QLabel('Data Save')
        label.setAlignment(Qt.AlignCenter)
        self.setLabelFont(label, 22, True)

        start_btn = QPushButton('Start')
        stop_btn = QPushButton('Stop')

        start_btn.setStyleSheet(style)
        stop_btn.setStyleSheet(style)

        #Event handler
        start_btn.clicked.connect(self.dataBase.startClicked)
        stop_btn.clicked.connect(self.dataBase.stopClicked)

        hbox.addWidget(start_btn)
        hbox.addWidget(stop_btn)

        vbox.addWidget(label, 1)
        vbox.addLayout(hbox, 2)

        return vbox


    def combobox_layout(self):
        #combobox style
        combo_style = "background-color:rgb(60,60,60);color:rgb(255,255,255);font-size:20px;"
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        label = QLabel('Selected Port')

        label.setAlignment(Qt.AlignCenter)
        self.setLabelFont(label, 22, True)

        cb = self.comboBox
        cb.addItem('None')
        
        cb.setStyleSheet(combo_style)
        cb.setSizePolicy(3,1)

        #set button
        button_style = "background-color:rgb(25,215,76);color:rgb(0,0,0);font-size:24px;"

        search_btn = QPushButton('Search')
        #connect_btn = QPushButton('Connect')
        

        search_btn.setStyleSheet(button_style)
        self.connect_btn.setStyleSheet(button_style)
        
        search_btn.clicked.connect(self.com.searchPort)
        self.connect_btn.clicked.connect(self.com.connectPort)

        hbox.addWidget(search_btn)
        hbox.addWidget(self.connect_btn)

        vbox.addWidget(label,1)
        vbox.addLayout(hbox,1)
        vbox.addWidget(cb,3)

        return vbox



    def setLabelFont(self, label, size, bold=False):
        label.setFont(self.customFont(size, bold))
        pal = label.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("white"))
        label.setPalette(pal)


    def customFont(self, fontsize, bold=False):
        font = QtGui.QFont()
        font.setPixelSize(fontsize)
        font.setBold(bold)
        return font

    def drawGraphs(self):
        if (self.com.isOpen()):
            try:
                data_table = self.com.getData()
                #self.camThread.run(self.camera.pixLabel)
                #self.camera.cameraLoad()

                if (len(data_table) == 7):
                    #print(data_table)

                    self.dioxid.update(data_table[1])
                    self.acc.update(data_table[2])
                    self.altitude.update(data_table[5])
                    self.algae.update(data_table[6])

                    self.mapbox.updateMap(data_table[0], data_table[3], data_table[4], data_table[5], data_table[6], self.algae)
                    self.dataBase.saveStart(data_table)
               
            
            except ValueError:
                pass #value error for Serial communication error


app = QApplication(sys.argv)
ex = GroundStationUI()


timer = pg.QtCore.QTimer()

timer.start(250) #250
timer.timeout.connect(ex.drawGraphs)


"""
if(ex.com.isOpen()):
    timer = pg.QtCore.QTimer()
    timer.start(250) #150
    timer.timeout.connect(ex.drawGraphs)

"""



if __name__ == '__main__':
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtWidgets.QApplication.instance().exec_()
        ex.com.close()
        #sys.exit(app.exec_())
    
    #sys.exit(app.exec_())


