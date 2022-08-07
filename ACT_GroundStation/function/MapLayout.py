
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from jinja2 import Template
import numpy as np

#from graphs import algae_status
import io
import folium # pip install folium
from datetime import datetime
import time

class MapLayout(QVBoxLayout):

    basemap = {
        'Google Satellite Hybrid': folium.TileLayer(
            tiles = 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
            attr = 'Google',
            name = 'Google Satellite',
            overlay = True,
            control = True
        ),

        'Google Satellite': folium.TileLayer(
            tiles = 'https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
            attr = 'Google',
            name = 'Google Satellite',
            overlay = True,
            control = True
        )

    }


    def __init__(self, latitude:float, longitude:float, zoom:int):
        super().__init__()

        self.mapView = QWebEngineView()
        self.zoom = zoom

        #Map view Location
        self.latitude = latitude
        self.longitude = longitude
        self.loadMap()
        time.sleep(1)
        
        #self.markLocation(self.latitude, self.longitude, 43)

    
    def loadMap(self):
        self.map = folium.Map(
            zoom_start=self.zoom,
            location=(self.latitude, self.longitude)
        )

        #set basemap
        self.basemap['Google Satellite'].add_to(self.map)

        folium.LayerControl().add_to(self.map)
        """
        folium.Marker(location=(self.latitude, self.longitude),
            icon=folium.Icon(color="red", icon="star"),
            popup="Location"
            
        ).add_to(self.map)
        
        """

        mapData = io.BytesIO()
        self.map.save(mapData, close_file=False)

        self.mapView.setHtml(mapData.getvalue().decode())
        self.addWidget(self.mapView)
        #self.map.save("GoogleMap.html")


    #def updateMap(self):

    def updateMap(self, date:str, latitude:str, longitude:str, altitude:str, isEject:str, algae_status):

        #Mark the Cansat Location using folium Marker
        if(latitude == None):
            return
        else:

            popup = """\'{}<br>Altitude:{}<br>Eject:{}\'""".format(date, altitude,"Eject Ready")
            icon = """CansatIcon"""


            if(algae_status.isEjected == True):
                popup = """\'{}<br>Altitude:{}<br>Eject:{}\'""".format(date, altitude,"Ejected")
                icon = """EjectedIcon"""

        
            js = Template(

            """
        
        var CansatIcon = L.icon({
            iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-gold.png',
            iconSize: [30, 50],
            iconAnchor: [10, 30],
            popupAnchor: [5, -30],
            shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
            shadowSize: [80, 35],
            shadowAnchor: [10, 30]
        });


        var EjectedIcon = L.icon({
            iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-red.png',
            iconSize: [30, 50],
            iconAnchor: [10, 30],
            popupAnchor: [5, -30],
            shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
            shadowSize: [80, 35],
            shadowAnchor: [10, 30]
        });


        L.marker([{{latitude}}, {{longitude}}], {icon: {{icon}}}).addTo({{map}}).bindPopup({{popup}});
        L.circleMarker(
            [{{latitude}}, {{longitude}}], {
                "bubblingMouseEvents": true,
                "color": "#5D5D5D",
                "dashArray": null,
                "dashOffset": null,
                "fill": false,
                "fillColor": "#5D5D5D",
                "fillOpacity": 0.2,
                "fillRule": "evenodd",
                "lineCap": "round",
                "lineJoin": "round",
                "opacity": 1.0,
                "radius": 2,
                "stroke": true,
                "weight": 5
            }
        ).addTo({{map}});
        
        """
            ).render(
                map=self.map.get_name(),
                latitude=latitude,
                longitude=longitude,
                popup=popup,
                icon=icon
            )
            self.mapView.page().runJavaScript(js)

        
    def getDate(self):
        now = datetime.now()
        date = now.strftime("%Y.%m.%d %H:%M %a")
        return date



#{{map}}.setView(new L.LatLng({{latitude}}, {{longitude}}), 18);





