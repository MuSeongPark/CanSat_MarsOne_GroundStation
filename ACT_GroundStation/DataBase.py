import numpy as np
import pandas as pd
from datetime import datetime

"""
#Data Table
[Date, CO2, Acceleration, latitude, longitude, Altitude]

"""


class DataBase():
    columns = ["Date", "CO2", "Acceleration", "Latitude", "Longitude", "Altitude", "Ejection"]
    def __init__(self):
        self.df = pd.DataFrame(columns=self.columns)
        self.isSaving = False


    def startClicked(self):
        self.isSaving = True
        return self.isSaving

    def stopClicked(self):
        self.isSaving = False
        self.df.to_excel("Cansat_Data.xlsx")

    def saveStart(self, data_table:list):
        if (self.isSaving):
            data_table[-1] = self.IntToBoolString(data_table[-1])
            self.df.loc[len(self.df)] = data_table

    #def saveStop(self):
        #if (self.isSaving == False):
            #self.df.to_excel("Cansat_Data.xlsx")


    def IntToBoolString(self, isEject:str):
        if (int(isEject) == True):
            return "Ejected"

        else:
            return np.NaN


