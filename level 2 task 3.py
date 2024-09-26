
import pandas as pd
import folium
from IPython.display import display
from sklearn.cluster import KMeans
data = pd.read_csv("/content/mohan.csv")
restaurant_names = data["Restaurant Name"]
latitude = data["Latitude"]
longitude = data["Longitude"]
X = data[["Latitude", "Longitude"]]
num_clusters = 5

kmeans = KMeans(n_clusters=num_clusters, random_state=42)
data["Cluster"] = kmeans.fit_predict(X)
map_center = [latitude.mean(), longitude.mean()]
restaurant_map = folium.Map(location=map_center, zoom_start=12)
cluster_colors = ['red', 'blue', 'green', 'purple', 'black']
for index, row in data.iterrows():
    restaurant_name = row["Restaurant Name"]
    latitude = row["Latitude"]
    longitude = row["Longitude"]
    cuisines = row["Cuisines"]
    rating = row["Aggregate rating"]
    cluster = row["Cluster"]

    popup_text = f"Restaurant: {restaurant_name}\nCuisines: {cuisines}\nRating: {rating}"
    marker = folium.Marker([latitude, longitude], popup=popup_text)
    marker.add_to(restaurant_map)
display(restaurant_map)
