import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('/content/mohan.csv')
rating_counts = dataset['Aggregate rating'].value_counts().sort_index()



most_common_rating_range = rating_counts.idxmax()

print("Most common rating range: "+ str(most_common_rating_range))

average_votes = dataset['Votes'].mean()

print("Average number of votes received by restaurants: "+str(average_votes))


plt.hist(rating_counts, bins=20, edgecolor='black')
plt.xlabel('Aggregate Rating')
plt.ylabel('Frequency')
plt.title('Distribution of Aggregate Ratings')
plt.show()
