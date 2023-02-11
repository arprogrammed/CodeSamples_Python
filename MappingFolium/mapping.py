import pandas
data = pandas.read_csv("Volcanoes.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
ele = list(data['ELEV'])
nam = list(data['NAME'])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
def clr(inte):
    if inte < 1600:
        return 'green'
    elif 1601 <= inte < 3000:
        return 'orange'
    else:
        return 'red'

import folium
map = folium.Map(location=[38, -99], tiles='Stamen Terrain', zoom_start=8)

pop = folium.FeatureGroup(name = 'Population')
vol = folium.FeatureGroup(name = 'Volcanos')

for lt, ln, el, nm in zip(lat, lon, ele, nam):
    iframe = folium.IFrame(html=html % (nm, nm, el), width=200, height=100)
    vol.add_child(folium.Circle(location=[lt, ln], popup=folium.Popup(iframe), fill_color=clr(el), color=clr(el), radius=400.0))

pop.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 
else 'red'}))

map.add_child(pop)
map.add_child(vol)
map.add_child(folium.LayerControl())

map.save("MyMap.html")