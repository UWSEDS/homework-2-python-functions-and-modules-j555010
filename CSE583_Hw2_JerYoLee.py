#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Problem 1
import pandas as pd
import io
import requests
import numpy as np

url = "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"
s = requests.get(url).content
ds = pd.read_csv(io.StringIO(s.decode('utf-8')))
df = pd.DataFrame(ds)
df = df.head(10)
df_east=df['Fremont Bridge East Sidewalk']
df_west=df['Fremont Bridge West Sidewalk']
df1 = pd.DataFrame({'Fremont Bridge East Sidewalk':df_east,'Fremont Bridge West Sidewalk':df_west})
df1


# In[19]:


#Problem 2 
from pandas import Series, DataFrame
test = DataFrame(np.arange(20.0).reshape(10,2),index=['0','1','2','3','4','5','6','7','8','9'],columns=['Fremont Bridge East Sidewalk','Fremont Bridge West Sidewalk'])

#The DataFrame contains only the columns that you specified as the second argument.
if df1.columns.all() == test.columns.all():
    print('true')

#The values in each column have the same python type
if df1.columns.dtype == test.columns.dtype:
    print('true')

#There are at least 10 rows in the DataFrame.
if len(test.index) >= 10:
    print('true')

