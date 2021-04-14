# Python code for my PANDS Project 2021
# Author: Gillian Kane-McLoughlin

import numpy as n
import matplotlib.pyplot as plt
import pandas as pd

'''Dataset info for quick reference:
1. sepal length in cm
2. sepal width in cm
3. petal length in cm
4. petal width in cm
5. class:
-- Iris Setosa
-- Iris Versicolour
-- Iris Virginica


fields = ['sepallength','sepalwidth','petallength','petalwidth','class'] # these are the column names

with open ('iris.csv', 'r') as dataset:
    df = pd.read_csv(dataset, usecols = fields) # trying to read in the data under each column separately

# Test 
# print (df.sepallength)

print ('The mean sepal length is ',df['sepallength'].mean())
print ('The mean sepal width is ',df['sepalwidth'].mean())
print ('The mean petal length is ',df['petallength'].mean())
print ('The mean petal length is ',df['petalwidth'].mean())

print (df.describe())
'''

df = pd.read_csv("irisdata.csv", header=None)
# Apply column names on the csv file
df.to_csv("irisdata.csv", header=["sepal_length", "sepal_width", "petal_length", "petal_width", "class"], index=False)
#Read in the data again with the new column names now added
df = pd.read_csv("irisdata.csv")


print ("General Statistics: ", df.describe())
print ("First 5 Rows: ", df.head(5))
print ("Last 5 Rows: ", df.tail(5))
print ("Shape of Dataset (rows, columns): ", df.shape)
print (df["class"].value_counts())

print ("Dataset for Class: Iris-setosa")
print (df.loc[df["class"] == "Iris-setosa"])
print ("Dataset for Class: Iris-versicolor")
print (df.loc[df["class"] == "Iris-versicolor"])
print ("Dataset for Class: Iris-virginica")
print (df.loc[df["class"] == "Iris-virginica"])

print("Covariance: ", df.cov()) #Ref: http://www.cse.msu.edu/~ptan/dmbook/tutorials/tutorial3/tutorial3.html
print("Correlation: ", df.corr()) #Ref: http://www.cse.msu.edu/~ptan/dmbook/tutorials/tutorial3/tutorial3.html

maxsepallength = df['sepal_length'].max()
maxsepalwidth = df['sepal_width'].max()
maxpetallength = df['petal_length'].max()
maxpetalwidth = df['petal_width'].max()
minsepallength = df['sepal_length'].min()
minsepalwidth = df['sepal_width'].min()
minpetallength = df['petal_length'].min()
minpetalwidth = df['petal_width'].min()

print ("Max sepal length & corresponding data:")
print (df.loc[df["sepal_length"] == maxsepallength])


