import folium
import pandas

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles=("Stamen Terrain"))

data = pandas.read_csv("mapping/Volcanoes.txt")
latitude = list(data["LAT"])
longitude = list(data["LON"])
volcano_name = list(data["NAME"])
elevation = list(data["ELEV"])


def marker_color(elevation):
    if elevation < 1500:
        return "green"
    elif elevation > 3000:
        return "red"
    else:
        return "orange"


fg = folium.FeatureGroup(name="My Map")

for lat, lon, name, elev in zip(latitude, longitude, volcano_name, elevation):
    fg.add_child(
        folium.CircleMarker(
            location=[lat, lon],
            radius=6,
            popup=str(name) + ": Elevation: " + str(elev) + "m",
            fill_color=marker_color(elev),
            color="black",
            fill_opacity=0.7,
        )
    )

fg.add_child(
    folium.GeoJson(data=(open("mapping/world.json", "r", encoding="utf-8-sig").read()))
)


map.add_child(fg)

map.save("Map1.html")
