
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

df = pd.read_csv('/Users/alikhan/Downloads/NetflixShows.csv',encoding = "ISO-8859-1")

#print the data set
print(df)



#drop the Na values from the user rating score for accurate data
df = df.dropna(subset = ["user rating score"])
print(df)


##factor the dataset into particular column
df1 = df.loc[df['rating'] == 'TV-14']
print(df1)

##Find the average of TV-14


df1 = df1['user rating score'].mean()
print("mean: ", df1)




#Locate the PG-13 Dataset

df2 = df.loc[df['rating'] == 'PG-13']
print(df2)


#Find the average of PG-13

df2 = df2['user rating score'].mean()
print("mean: ",df2)





#Locate the rating Dataset

df3 = df.loc[df['rating'] == 'R']
print(df3)


#Find the average of Rating set

df3 = df3['user rating score'].mean()
print("mean: ", df3)








