#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
df = pd.read_csv(r'C:\Users\Dhruv Bajaj\Downloads\winequality\winequality-red.csv', sep=';')
df.head()

## Renaming Columns

df.columns = [label.replace(' ', '_') for label in df.columns]
df.head()

## Analyzing Features

def numeric_to_buckets(df, column_name):
    median = df[column_name].median()
    for i, val in enumerate(df[column_name]):
        if val >= median:
            df.loc[i, column_name] = 'high'
        else:
            df.loc[i, column_name] = 'low' 

for feature in df.columns[:-1]:
    numeric_to_buckets(df, feature)
    print(df.groupby(feature).quality.mean(), '\n')


# In[ ]:




