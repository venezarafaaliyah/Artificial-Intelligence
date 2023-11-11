# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 15:33:36 2022

@author: ACER
"""

import pandas as pd  
data = {'apples': [3, 2, 0, 1], 'oranges': [0, 3, 7, 2]}
df1 = pd.DataFrame(data)
df1 = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])
df1.loc['June']

pur_df = pd.read_csv('purchases.csv’)
pur_df = pd.read_csv('purchases.csv', index_col=0)

movies_df = pd.read_csv("IMDB-Movie-Data2.csv", index_col="Title")
movies_df.head()
movies_df.head(7)
movies_df.tail(2)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

movies_df.info()
movies_df.shape

import pandas as pd  
movies_df = pd.read_csv("IMDB-Movie-Data2.csv", index_col="Title")
temp_df = movies_df.append(movies_df)
print(temp_df.shape)
temp_df.drop_duplicates(inplace=True)

movie_df.columns
movies_df.rename(columns={ 'Runtime (Minutes)': 'Runtime', 'Revenue (Millions)': 'Revenue_millions'}, inplace=True) 

movies_df.columns = ['rank', 'genre', 'description', 'director', 'actors', 'year', 'runtime', 'rating', 'votes', 'revenue_millions', 'metascore']

movies_df.columns = [col.lower() for col in movies_df]

a = movies_df.isnull()
nullmovies_df.isnull().sum()
new_df = movies_df.dropna()
new_df.isnull().sum()

movies.df.dropna(axis=1)
import pandas as pd
movies_df = pd.read_csv("IMDB-Movie-Data2.csv", index_col="Title")
revenue = movies_df['Revenue (Millions)']
revenue.head()
revenue_mean = revenue.mean()
newRevenue = revenue.fillna(revenue_mean) 
revenue.fillna(revenue_mean, inplace = True)  
print('Original revenue: ', revenue.isnull().sum())
print('New revenue: ', newRevenue.isnull().sum())


import pandas as pd
movies_df = pd.read_csv("IMDB-Movie-Data2.csv", index_col="Title")
revenue = movies_df['Revenue (Millions)']
revenue.head()
revenue_mean = revenue.mean()
revenue.fillna(revenue_mean, inplace = True)   
metascore_mean = movies_df['Metascore'].median()movies_df['Metascore'].fillna(metascore_mean, inplace = True)print(movies_df.isnull().sum())

movies_df.describe()
movies_df['Genre'].describe()
movies_df['Genre'].value_counts().head(10)

movies_df.corr()

genre_col = movies_df['Genre'] 
type(genre_col)genre_col = movies_df[['Genre']]
Type(genre_col)subset = movies_df[['Rank', 'Genre', 'Year']]



