

#from email.charset import QP
#from tokenize import String
#import random
import serial
import serial.tools.list_ports
import time
#import numpy as np

from PyQt5.QtWidgets import QComboBox, QPushButton
from datetime import datetime


class Communication:
    baudrate = ''
    portName = ''
    ports = serial.tools.list_ports.comports()
    ser = serial.Serial()
    def __init__(self, baudrate:int, comboBox:QComboBox, connect_btn:QPushButton):
        self.baudrate = baudrate
        self.cbBox = comboBox
        self.isConnected = 0
        self.connect_btn = connect_btn
        #self.searchPort()
        """
        print("The available ports are :")
        for port in sorted(self.ports):
            print("{}".format(port))
            #self.comboBox.addItem(portName[0])
        self.portName = input("write serial port name : ")
        try:
            self.ser = serial.Serial(self.portName, 9600)
            time.sleep(1)
        except serial.serialutil.SerialException:
            print("Error Can't Open : ", self.portName)

        """

    def searchPort(self):
        self.ports = serial.tools.list_ports.comports()
        self.cbBox.clear()
        for port in sorted(self.ports):
            
            portSplit = str(port).split("-")
            self.cbBox.addItem(portSplit[:-1][0])

    def connectPort(self):
        if (self.isConnected == False):
            portName = self.cbBox.currentText()

            try:
                self.ser = serial.Serial(portName, self.baudrate)
                self.isConnected = 1
                self.connect_btn.setText("Connected")
                time.sleep(1)
            

            except serial.SerialException:
                print("Can't Open : ", portName)
                self.connect_btn.setText("Connect")

        else:
            self.close()
            self.isConnected = 0
            self.connect_btn.setText("Connect")



    def close(self):
        if(self.ser.isOpen()):
            self.ser.close()

    def getData(self):
        if (self.ser.inWaiting() > 0):
        
            value = self.ser.readline()
            #value = self.sio.readline()
            decoded = str(value[0:len(value) - 2].decode("utf-8"))
            value_table = decoded.split(",")
        #print(value_chain)
            value_table = self.LatLongiModify(value_table)
            value_table.insert(0, self.getDate())
        else:
            value_table = []
            
        return value_table

    def getDate(self):
        now = datetime.now()
        date = now.strftime("%Y-%m-%d %H:%M:%S")
        return date

    
    def isOpen(self):
        return self.ser.isOpen()


    def LatLongiModify(self, value_table:list):
        if (value_table[2] == 'n'):
            value_table[2] = None
            value_table[3] = None
            return value_table
        else:
            return value_table
