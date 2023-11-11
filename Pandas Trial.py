# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 21:46:12 2022

@author: ACER
"""

import numpy as np
import pandas as pd

data = {'apples': [3, 2, 0, 1], 'oranges': [0, 3, 7, 2]}
df1 = pd.DataFrame(data)
df1 = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])
df1.loc['June']

pur_df = pd.read_csv('purchases.csv')
pur_df = pd.read_csv('purchases.csv', index_col=0)

pur_df = pd.read_csv("purchases.csv")
pur_df = pd.read_csv("purchases.csv", index_col=0)
pur_df

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
movies_df.head()
movies_df.tail()
movies_df.info()

movies_df.columns
movies_df.rename(columns={ 'Runtime (Minutes)': 'Runtime', 'Revenue (Millions)': 'Revenue_millions'}, inplace=True) 

