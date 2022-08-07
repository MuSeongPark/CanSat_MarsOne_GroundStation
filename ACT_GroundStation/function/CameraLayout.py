from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget

from PyQt5.QtGui import QPixmap

from selenium import webdriver
import os

class CameraLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.path = "C:/Users/HP DEMO HUB/Downloads"

        file_list = os.listdir(self.path)
        pixmap = QPixmap(self.path+ "/"+ file_list[-1])

        self.pixLabel = QLabel()
        #self.pixLabel.resize(500, 300)

        self.pixLabel.setPixmap(pixmap)
        self.pixLabel.setVisible(True)
        

        self.addWidget(self.pixLabel, alignment=Qt.AlignCenter)
        #self.indx = 0
        
        #self.cameraLoad()
    """
    def cameraLoad(self):
        if(self.indx < 5):
            file_list = os.listdir(self.path)
            pixmap = QPixmap(self.path + "/" + file_list[-1])
            self.pixLabel.setPixmap(pixmap)
            #self.pixLabel.setVisible(True)
            #self.pixLabel.repaint()
            self.indx += 1
        else:
            self.indx = 0

    
    """



    """
    def cameraLoad(self):
        webView = QWebEngineView()
        #webView.load(QUrl("http://192.168.0.4"))
        webView.load(QUrl("http://192.168.213.30"))

        self.addWidget(webView)

    """

    