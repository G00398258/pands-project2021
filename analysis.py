# Python code for my PANDS Project 2021
# Author: Gillian Kane-McLoughlin

import numpy as n
import matplotlib.pyplot as plt
import pandas as pd
import sys

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

# Read in the raw data
df = pd.read_csv("iris.csv", header=None)
# Apply column names on the csv file
df.to_csv("iris.csv", header=["sepal_length", "sepal_width", "petal_length", "petal_width", "class"], index=False)
# Read in the data again with the new column names now added
df = pd.read_csv("iris.csv")

# Analysis
def analysis():
    original_stdout = sys.stdout # Code taken from: https://stackabuse.com/writing-to-a-file-with-pythons-print-function/

    df = pd.read_csv("iris.csv")
    f = open("analysis.csv", "a")
    sys.stdout = f
    print ("General Statistics: \n", df.describe())
    print("\n") # adding an empty line between each data point to make it look and read a bit better
    print ("First 5 Rows: \n", df.head(5))
    print("\n")
    print ("Last 5 Rows: \n", df.tail(5))
    print("\n")
    print ("Shape of Dataset (rows, columns): ", df.shape)
    print("\n")
    print (df["class"].value_counts())
    print("\n")

    print ("Dataset for Class: Iris-setosa")
    print (df.loc[df["class"] == "Iris-setosa"])
    print("\n")
    print ("Dataset for Class: Iris-versicolor")
    print (df.loc[df["class"] == "Iris-versicolor"])
    print("\n")
    print ("Dataset for Class: Iris-virginica")
    print (df.loc[df["class"] == "Iris-virginica"])
    print("\n")

    print("Covariance: \n", df.cov()) #Ref: http://www.cse.msu.edu/~ptan/dmbook/tutorials/tutorial3/tutorial3.html
    print("\n")
    print("Correlation: \n", df.corr()) #Ref: http://www.cse.msu.edu/~ptan/dmbook/tutorials/tutorial3/tutorial3.html
    print("\n")


    maxsepallength = df['sepal_length'].max()
    maxsepalwidth = df['sepal_width'].max()
    maxpetallength = df['petal_length'].max()
    maxpetalwidth = df['petal_width'].max()
    minsepallength = df['sepal_length'].min()
    minsepalwidth = df['sepal_width'].min()
    minpetallength = df['petal_length'].min()
    minpetalwidth = df['petal_width'].min()

    modesepallength = df['sepal_length'].mode()
    modesepalwidth = df['sepal_width'].mode()
    modepetallength = df['petal_length'].mode()
    modepetalwidth = df['petal_width'].mode()

    mediansepallength = df['sepal_length'].median()
    mediansepalwidth = df['sepal_width'].median()
    medianpetallength = df['petal_length'].median()
    medianpetalwidth = df['petal_width'].median()

    #maxvalues = df.groupby('class').max()
    #print (maxvalues)

    # Print out index position and class of flower with min / max attributes
    print ("Largest Sepal Length: ", maxsepallength)
    print ("Index Position & Class of flower with largest Sepal Length:")
    print (df.loc[df["sepal_length"] == maxsepallength,"class"])
    print("\n")
    print ("Smallest Sepal Length: ", minsepallength)
    print ("Index Position & Class of flower with smallest Sepal Length:")
    print (df.loc[df["sepal_length"] == minsepallength,"class"])
    print("\n")
    print ("Largest Sepal Width: ", maxsepalwidth)
    print ("Index Position & Class of flower with largest Sepal Width:")
    print (df.loc[df["sepal_width"] == maxsepalwidth,"class"])
    print("\n")
    print ("Smallest Sepal Width: ", minsepalwidth)
    print ("Index Position & Class of flower with smallest Sepal Width:")
    print (df.loc[df["sepal_width"] == minsepalwidth,"class"])
    print("\n")
    print ("Largest Petal Length: ", maxpetallength)
    print ("Index Position & Class of flower with largest Petal Length:")
    print (df.loc[df["petal_length"] == maxpetallength,"class"])
    print("\n")
    print ("Smallest Petal Length: ", minpetallength)
    print ("Index Position & Class of flower with smallest Petal Length:")
    print (df.loc[df["petal_length"] == minpetallength,"class"])
    print("\n")
    print ("Largest Petal Width: ", maxpetalwidth)
    print ("Index Position & Class of flower with largest Petal Width:")
    print (df.loc[df["petal_width"] == maxpetalwidth,"class"])
    print("\n")
    print ("Smallest Petal Width: ", minpetalwidth)
    print ("Index Position & Class of flower with smallest Petal Width:")
    print (df.loc[df["petal_width"] == minpetalwidth,"class"])
    print("\n")
    sys.stdout = original_stdout
    return print ("Analysis has been completed. Please see file analysis.csv")

''' Mode
print ("Mode of Sepal Length: ", modesepallength)
print ("Corresponding Index & Class:")
print (df.loc[df["sepal_length"] == modesepallength,"class"])
print("\n")
print ("Mode of Sepal Width: ", modesepalwidth)
print ("Corresponding Index & Class:")
print (df.loc[df["sepal_width"] == modesepalwidth,"class"])
print("\n")
print ("Mode of Petal Length: ", modepetallength)
print ("Corresponding Index & Class:")
print (df.loc[df["petal_length"] == modepetallength,"class"])
print("\n")
print ("Mode of Petal Width: ", modepetalwidth)
print ("Corresponding Index & Class:")
print (df.loc[df["petal_width"] == modepetalwidth,"class"])
print("\n")
'''
analysis()