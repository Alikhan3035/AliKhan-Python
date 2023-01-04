

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
df = pd.read_csv('/Users/alikhan/Downloads/NetflixShows.csv',encoding = "ISO-8859-1")



#drop dataset from previous one

df = df.dropna(subset = ['user rating score'])
print(df)




#printing all the rating in the column
ratings = df['rating'].unique()
rate = []
print(ratings)



#locates the Rating of each dataset and find the average of all the values
for r in ratings: 
    temp = df.loc[df['rating'] == r]
    rate.append((r, round((temp['user rating score'].mean()), 2)))


#Sorting the data based on scores set in order from smallest to largest on graph


for i in range(len(rate)):
    for j in range(0, len(rate) - i - 1):
        if(rate[j][1] > rate[j+1][1]):
            rate[j], rate[j + 1] = rate[j + 1], rate[j]


# grouping the values of x and y sides


x_axis = []
y_axis = []
for r in rate: 
    x_axis.append(r[0])
    y_axis.append(r[1])

# plotting the chart 

plt.bar(x_axis, y_axis)
plt.title("Ratings and their Average Scores")
plt.xlabel("Ratings")
plt.ylabel("Average Score")
plt.gcf().set_size_inches(12, 10)
plt.show()




