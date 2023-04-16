import folium
import pandas as pd

data = pd.read_csv('Volcanoes.txt')
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def set_marker_colour(elevation):
    if elevation < 1000:
        return 'green'
    elif elevation < 2500:
        return 'orange'
    else:
        return 'red'

fg1 = folium.FeatureGroup('GRUPA 1')
fg2 = folium.FeatureGroup('Grupa 2')

mapa = folium.Map(
    location=[42.5941512,-117.4363148],
    zoom_start = 5
)

for lt,ln,el in zip(lat,lon,elev) :
    folium.CircleMarker([lt,ln],radius=5,popup=str(el) + ' meaters :',color="gray",fill=True,fill_color =set_marker_colour(el),fill_opacity = 10).add_to(mapa)

fg2.add_to(mapa)
folium.GeoJson(data=open("world.json","r", encoding="utf-8-sig").read(),
               style_function= lambda x:{
                   'fillColor': 'green' if x['properties']['POP2005']<1000000
                   else 'yellow' if x['properties']['POP2005']<4500000
                   else 'red'
               }).add_to(mapa)
fg2.add_to(mapa)
fg1.add_to(mapa)
folium.LayerControl().add_to(mapa)

mapa.save("zad5.html")