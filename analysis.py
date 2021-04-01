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
'''

fields = ['sepallength','sepalwidth','petallength','petalwidth','class'] # these are the column names

with open ('iris.csv', 'r') as dataset:
    df = pd.read_csv(dataset, usecols = fields) # trying to read in the data under each column separately

# Test 
# print (df.sepallength)

print ('The mean sepal length is ',df['sepallength'].mean())
print ('The mean sepal width is ',df['sepalwidth'].mean())
print ('The mean petal length is ',df['petallength'].mean())
print ('The mean petal length is ',df['petalwidth'].mean())

