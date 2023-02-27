"""
Date - FEb 16 2023
Students - Jahnavi, Indupriya, Tarani.
"""
# pandas
x = 1
var = 'Python'
list1 = [1, 'Python', 3.1416]

# Basic python - python.org
# pip install pandas==1.1.2
# Jupyter notebook - pandas is readily available.
import pandas as pd
import numpy as np

df = pd.DataFrame()
df['name'] = ['Santosh', 'Manideep', 'Jahnavi', 'Indupriya', 'Tarani']
df['sletters'] = ['S', 'M', 'J', 'I', 'T']
df.to_csv('names_new.csv', index=False)
print(df.dtypes)
df['SSN'] = [111,222,333,444,555]
print(df)


# print(df.iloc[3]['SSN'])
df.head() # first 5 rows
df.tail() # last 5 rows

df.size # total columns x rows
len(df) # number of rows
df_new = pd.DataFrame({'dates': ['2023-02-16', '2023-02-16', '2023-02-16', '2023-02-16']})
df_new['names'] = ['Manideep', 'Jahnavi', 'Indupriya', 'Tarani']
dfmerged = pd.merge(df, df_new, left_on='name', right_on='names', how='outer')
