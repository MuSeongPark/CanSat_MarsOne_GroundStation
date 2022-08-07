import pydeck as pdk
#import os
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import pandas as pd

# Import Mapbox API Key from environment
#MAPBOX_API_KEY = "pk.eyJ1IjoicG1zMzYyMCIsImEiOiJjbDU1N290cHAwMjlnM2hrOHYxZ2s2eHI4In0.DPHqfz1P7WEyIQszVlnQSg"
#mapbox_key_dict = {"mapbox": MAPBOX_API_KEY}



class MapLayout(QVBoxLayout):
    mapbox_api_key = "pk.eyJ1IjoicG1zMzYyMCIsImEiOiJjbDU1N290cHAwMjlnM2hrOHYxZ2s2eHI4In0.DPHqfz1P7WEyIQszVlnQSg"
    mapbox_key_dict = {"mapbox": mapbox_api_key}


    def __init__(self, latitude, longitude, zoom):
        super().__init__()
        self.latitude = latitude
        self.longitude = longitude
        self.zoom = zoom
        self.mapLoad()
    
    def mapLoad(self):
        self.view_state = pdk.ViewState(latitude=self.latitude, longitude=self.longitude, zoom=self.zoom)

        self.deck = pdk.Deck(layers=[],
                initial_view_state=self.view_state,
                api_keys=self.mapbox_key_dict,
                map_provider="mapbox",
                map_style='road')

        self.deck.to_html("Map.html")
        
        webView = QWebEngineView()

        webView.load(QUrl("file:///C:/Users/HP%20DEMO%20HUB/Desktop/ACT%20GCS/Map.html"))
        #webView.setHtml(baseUrl= QUrl("file:///C:/Users/HP%20DEMO%20HUB/Desktop/ACT%20GCS/Map.html"))

        self.addWidget(webView)

    def mapUpdate(self):
        ICON = "Mapicon.png"
        icon_data = {
            "url":ICON,
            "width":242,
            "height":242,
            "anchorY":242,
        }

        

        icon_layer = pdk.Layer(
            type="IconLayer",
            get_icon=icon_data,
            get_position=[35.153831,128.097320],
            pickable=True,
        )

        self.deck(layers=[icon_layer], initial_view_state=self.view_state,
                api_keys=self.mapbox_key_dict,
                map_provider="mapbox",
                map_style='road')
        self.deck.update()



        

        





#view_state = pdk.ViewState(latitude=35.15688919999978, longitude=128.09505469999976, zoom=12)



