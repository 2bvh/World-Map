import folium
import pandas

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles=("Stamen Terrain"))

data = pandas.read_csv("mapping/Volcanoes.txt")
latitude = list(data["LAT"])
longitude = list(data["LON"])
volcano_name = list(data["NAME"])
elevation = list(data["ELEV"])


fg = folium.FeatureGroup(name="My Map")

for lat, lon, name, elev in zip(latitude, longitude, volcano_name, elevation):
    fg.add_child(
        folium.Marker(
            location=[lat, lon],
            popup=str(name) + ": Elevation: " + str(elev) + "m",
            icon=folium.Icon(color="green"),
        )
    )
map.add_child(fg)

map.save("Map1.html")
