'''Various operations on pandas dataframe and series'''

import pandas as pd

col_names = ['Id','Age','Gender','Occupation','Zip-code']

table = pd.read_table("http://bit.ly/movieusers", sep ='|', header = None, names = col_names)
print(table)

n = 10
print(table.head(n))    #Read first n lines, default n=5

print(type(table))      #Pandas Dataframe

df = pd.read_csv("http://bit.ly/uforeports", )
print(type(df['City']))

df['location'] = df.City +" , " + df.State          #Adding a new column
print(df.location)

print(df.columns)

df.rename(columns = {'City':'Cities'}, inplace = True)
print(df.columns)

df.columns = df.columns.str.replace(" ","_")
print(df.columns)
print(df.shape)

df.drop('Cities', axis = 1, inplace = True)
print(df.shape)

df.drop([2,3], axis = 0, inplace = True)
print(df.shape)

