import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("/content/mohan.csv")
restaurant_with_highest_votes = data.loc[data["Votes"].idxmax()]
restaurant_with_lowest_votes = data.loc[data["Votes"].idxmin()]
print(data.head())
restaurant_with_highest_votes = data.loc[data["Votes"].idxmax()]
restaurant_with_lowest_votes = data.loc[data["Votes"].idxmin()]
print("Restaurant with the highest number of votes:")
print(restaurant_with_highest_votes)
print("\nRestaurant with the lowest number of votes:")
print(restaurant_with_lowest_votes)
data["Votes"] = pd.to_numeric(data["Votes"])
data["Aggregate rating"] = pd.to_numeric(data["Aggregate rating"])
correlation = data["Votes"].corr(data["Aggregate rating"])
print("\nCorrelation between number of votes and rating:", correlation)
plt.scatter(data["Votes"], data["Aggregate rating"])
plt.xlabel("Number of Votes")
plt.ylabel("Aggregate rating")
plt.title("Correlation between Number of Votes and Restaurant Rating")
plt.show()