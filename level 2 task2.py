import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("/content/mohan.csv")

cuisines = data["Cuisines"]

aggregate_ratings = data["Aggregate rating"]


most_common_cuisine_combinations = cuisines.value_counts().head(10)
print("Most common cuisine combinations:")
print(most_common_cuisine_combinations)
cuisine_combinations_avg_rating = data.groupby("Cuisines")["Aggregate rating"].mean()
top_10_avg_ratings = cuisine_combinations_avg_rating.nlargest(10)
print("\nAverage ratings for the top 10 cuisine combinations:")
print(top_10_avg_ratings)