from pathlib import Path
import sys
 
#from datetime import datetime
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import *
#from PyQt5.QtGui import QPixmap
import os
from selenium.webdriver.common.by import By

import time
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui


from selenium import webdriver
class ThreadClass(QThread): 
    def __init__(self, parent = None): 

        super(ThreadClass,self).__init__(parent)
        self.driver = webdriver.Chrome("C:/Users/HP DEMO HUB/Desktop/ACT GCS/Ground_Control_System/picture/chromedriver.exe")

        self.driver.get("http://192.168.0.3")
        elem = self.driver.find_element(By.ID, "toggle-stream")
        #elem = self.driver.find_element_by_id("toggle-stream")
        elem.click()


        self.cnt = 0



        #camLayout
        self.path = "C:/Users/HP DEMO HUB/Downloads"


    def run(self, pixLabel:QLabel):

        self.cnt += 1
        if(self.cnt == 10): #every 5second (Since every 250ms) 
            elem = self.driver.find_element(By.ID, "save-still")
            #elem = self.driver.find_element_by_id("save-still") #
            elem.click()#
            


            file_list = os.listdir(self.path)
            if (file_list[-2] != "desktop.ini" and Path(self.path+"/"+file_list[-2])):
                pixmap = QPixmap(self.path + "/" + file_list[-2])
                #print(file_list[-2])
                

                pixmap = pixmap.transformed(QtGui.QTransform().rotate(90))
                pixmap = pixmap.scaled(400,330)
                pixLabel.setPixmap(pixmap)
                pixLabel.setVisible(True)
                #pixLabel.repaint()

        if(self.cnt == 20):
            
            elem = self.driver.find_element(By.ID, "toggle-stream")
            elem.click()
            elem.click()
            self.cnt = 0

            

