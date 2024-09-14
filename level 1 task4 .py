import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('/content/mohan.csv')
total_restaurants = len(dataset)
restaurants_with_online_delivery = dataset['Has Online delivery'].value_counts().get('Yes', 0)
percentage_with_online_delivery = (restaurants_with_online_delivery / total_restaurants) * 100
print("Percentage of restaurants that offer online delivery:", percentage_with_online_delivery)
average_rating_with_online_delivery = dataset[dataset['Has Online delivery'] == 'Yes']['Aggregate rating'].mean()
average_rating_without_online_delivery = dataset[dataset['Has Online delivery'] == 'No']['Aggregate rating'].mean()
print("Average rating of restaurants with online delivery:", average_rating_with_online_delivery)
print("Average rating of restaurants without online delivery:", average_rating_without_online_delivery)
labels = ['With Online Delivery', 'Without Online Delivery']
average_ratings = [average_rating_with_online_delivery, average_rating_without_online_delivery]

plt.bar(labels, average_ratings)
plt.xlabel('Online Delivery')
plt.ylabel('Average Rating')
plt.title('Comparison of Average Ratings')
plt.show()
