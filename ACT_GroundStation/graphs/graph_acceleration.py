import pyqtgraph as pg
import numpy as np

class graph_acceleration(pg.PlotWidget):
    def __init__(self):
        super().__init__()
        self.setTitle('Acceleration', color='w', size='18pt')
        self.setLabel('left', 'Acceleration (g)')
        self.setLabel('bottom', 'Time(s)')
        
        #graph style
        pen = pg.mkPen(color=(0, 84, 255), width=2)
        
        #set graph data
        self.x = np.linspace(0,1,20)
        self.y = np.linspace(0,0,20)
        self.plot = self.plot(self.x, self.y, pen=pen)

    
    def update(self, value):
        x = self.x[-1]
        self.x[:-1] = self.x[1:]
        self.x[-1] = x+0.25 #Since update graph every 0.25sec

        self.y[:-1] = self.y[1:] #데이터 테이블 이동
        self.y[-1] = float(value) #마지막에 새로운 데이터 추가

        self.plot.setData(self.x, self.y)
