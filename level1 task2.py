import pandas as pd
df = pd.read_csv('/content/mohan.csv')
print(df.head())

city_counts = df['City'].value_counts()
city_with_most_restaurants = city_counts.index[0]

print(f"City with the highest number of restaurants: {city_with_most_restaurants}")

average_ratings_by_city = df.groupby('City')['Aggregate rating'].mean()
print("Average ratings for restaurants in each city:")
print(average_ratings_by_city)

city_with_highest_average_rating = average_ratings_by_city.idxmax()
print(f"City with the highest average rating: {city_with_highest_average_rating}")