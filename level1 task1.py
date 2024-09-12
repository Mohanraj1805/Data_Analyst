import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Dataset .csv')
print(df.head())
cuisine_counts = df['Cuisines'].value_counts()
cuisines = cuisine_counts.head(3)
restaurants = len(df)
percentages = (cuisines / restaurants) * 100
import numpy as np
colors = ['black', 'blue', 'brown']
plt.bar(cuisines.index, cuisines.values, color=colors)
plt.xlabel('Cuisine')
plt.ylabel('Count')
plt.title('Top Three Cuisines')
plt.show()
plt.pie(cuisines.values, labels=cuisines.index, autopct='%1.1f%%')
plt.title('Top Three Cuisines')
plt.show()