import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("/content/mohan.csv")
restaurant_chains = data.groupby("Restaurant Name").size().reset_index(name="Chain Count")
restaurant_chains = restaurant_chains[restaurant_chains["Chain Count"] > 1]
restaurant_chains = restaurant_chains.sort_values(by="Chain Count", ascending=False)
plt.figure(figsize=(10, 6))
plt.bar(restaurant_chains["Restaurant Name"][:10], restaurant_chains["Chain Count"][:10])
plt.xticks(rotation=45, ha='right')
plt.xlabel("Restaurant Chain")
plt.ylabel("Number of Outlets")
plt.title("Top 10 Restaurant Chains by Number of Outlets")
plt.tight_layout()
plt.show()

chain_ratings = data.groupby("Restaurant Name")["Aggregate rating"].mean().reset_index(name="Average Rating")
chain_votes = data.groupby("Restaurant Name")["Votes"].sum().reset_index(name="Total Votes")
chain_analysis = pd.merge(chain_ratings, chain_votes, on="Restaurant Name")
chain_analysis = chain_analysis.sort_values(by="Average Rating", ascending=False)
plt.figure(figsize=(10, 6))
plt.bar(chain_analysis["Restaurant Name"][:10], chain_analysis["Average Rating"][:10])
plt.xticks(rotation=45, ha='right')
plt.xlabel("Restaurant Chain")
plt.ylabel("Average Rating")
plt.title("Top 10 Restaurant Chains by Average Rating")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(chain_analysis["Restaurant Name"][:10], chain_analysis["Total Votes"][:10])
plt.xticks(rotation=45, ha='right')
plt.xlabel("Restaurant Chain")
plt.ylabel("Total Votes")
plt.title("Top 10 Restaurant Chains by Total Votes")
plt.tight_layout()
plt.show()

print("Top 10 Restaurant Chains by Number of Outlets:")
print(restaurant_chains[["Restaurant Name", "Chain Count"]].head(10))

print("\nTop 10 Restaurant Chains by Total Votes:")
print(chain_analysis[["Restaurant Name", "Total Votes"]].head(10))