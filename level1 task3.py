import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('/content/mohan.csv')

price_range_counts = dataset['Price range'].value_counts().sort_index()
total_restaurants = len(dataset)
percentage_per_price_range = (price_range_counts / total_restaurants) * 100
plt.bar(price_range_counts.index, price_range_counts.values)
plt.xlabel('Price Range')
plt.ylabel('Count')
plt.title('Distribution of Price Ranges')
plt.show()
print("Percentage of restaurants in each price range category:")
print(percentage_per_price_range)