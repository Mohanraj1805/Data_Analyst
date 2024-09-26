import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("/content/mohan.csv")
price_ranges = data["Price range"].unique()
online_delivery_percentages = []
for price_range in price_ranges:
    restaurants_with_delivery = data[(data["Price range"] == price_range) & (data["Has Online delivery"] == True)]
    total_restaurants = len(data[data["Price range"] == price_range])
    percentage_with_delivery = (len(restaurants_with_delivery) / total_restaurants) * 100
    online_delivery_percentages.append(percentage_with_delivery)
table_booking_percentages = []
for price_range in price_ranges:
    restaurants_with_table_booking = data[(data["Price range"] == price_range) & (data["Has Table booking"] == True)]
    total_restaurants = len(data[data["Price range"] == price_range])
    percentage_with_table_booking = (len(restaurants_with_table_booking) / total_restaurants) * 100
    table_booking_percentages.append(percentage_with_table_booking)
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.bar(price_ranges, online_delivery_percentages)
plt.xlabel("Price range")
plt.ylabel("Has Online delivery")
plt.title("Percentage of Restaurants with Online delivery by Price Range")

plt.subplot(1, 2, 2)
plt.bar(price_ranges, table_booking_percentages)
plt.xlabel("Price range")
plt.ylabel("Percentage with Has Table booking")
plt.title("Percentage of Restaurants with Table Booking by Price Range")

