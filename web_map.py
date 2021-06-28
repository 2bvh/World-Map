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


fgv = folium.FeatureGroup(name="Volcanoes")

for lat, lon, name, elev in zip(latitude, longitude, volcano_name, elevation):
    fgv.add_child(
        folium.CircleMarker(
            location=[lat, lon],
            radius=6,
            popup=str(name) + ": Elevation: " + str(elev) + "m",
            fill_color=marker_color(elev),
            color="black",
            fill_opacity=0.7,
        )
    )

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(
    folium.GeoJson(
        data=open("mapping/world.json", "r", encoding="utf-8-sig").read(),
        style_function=lambda x: {
            "fillColor": "green"
            if x["properties"]["POP2005"] < 1000000
            else "orange"
            if 1000000 <= x["properties"]["POP2005"] < 2000000
            else "red"
        },
    )
)


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
