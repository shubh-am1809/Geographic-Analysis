import pandas as pd
import folium
from folium.plugins import MarkerCluster

df = pd.read_csv("dataset .csv")
df = df[['Latitude', 'Longitude']].dropna()

map_center = [df['Latitude'].mean(), df['Longitude'].mean()]
restaurant_map = folium.Map(location=map_center, zoom_start=5)
marker_cluster = MarkerCluster().add_to(restaurant_map)
for _, row in df.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']]
    ).add_to(marker_cluster)
restaurant_map.save("output/restaurant_locations_map.html")

print("Map saved as output/restaurant_locations_map.html")
