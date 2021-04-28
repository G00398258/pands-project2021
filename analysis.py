# Code for the PANDS Project
# Author: Gillian Kane-McLoughlin

import matplotlib.pyplot as plt
import pandas as pd
import sys
import shutil
import seaborn as sns

file = "dataforproject.csv"
# Copying data from raw dataset to a new file, as I will be adding columns names and an index later on
shutil.copyfile("iris.data", file)
# reading in the data on this new file to create an intial dataframe
df = pd.read_csv(file, header=None) 
# Adding column names on the csv file
df.to_csv(file, header=["sepal_length", "sepal_width", "petal_length", "petal_width", "class"])

# Summary function - this will output a summary of each variable to a file called summary.txt
def summary():
    file = "dataforproject.csv"
    original_stdout = sys.stdout # Code copied from: https://stackabuse.com/writing-to-a-file-with-pythons-print-function/
    # Reading in the data within the function & setting the index column so I don't get an unnamed column in my output (lecture on pandas helped here!)
    df = pd.read_csv(file, index_col=0) 
    f = open("summary.txt", "a")
    sys.stdout = f # this will output print commands to the summary.txt file (which I have called f)

    print ("Iris Dataset Summary")
    print("\n")

    # General summary points: describe, head, tail, shape, value counts, covariance & correlation functions
    print ("General Statistics: \n", df.describe())
    print("\n") # adding an empty line between each data point to make it look and read a bit better
    print ("First 5 Rows of the Dataset: \n", df.head(5))
    print("\n")
    print ("Last 5 Rows of the Dataset: \n", df.tail(5))
    print("\n")
    print ("Shape of Dataset (# rows, # columns): ", df.shape)
    print("\n")
    print ("Value Counts for each Class: \n",df["class"].value_counts())
    print("\n")
    print("Covariance Between the Attributes: \n", df.cov())
    print("\n")
    print("Correlation Between the Attributes: \n", df.corr()) 
    print("\n")
    
    # Setting some variables before I move onto some more specific analysis
    maxsepallength = df['sepal_length'].max()
    maxsepalwidth = df['sepal_width'].max()
    maxpetallength = df['petal_length'].max()
    maxpetalwidth = df['petal_width'].max()
    minsepallength = df['sepal_length'].min()
    minsepalwidth = df['sepal_width'].min()
    minpetallength = df['petal_length'].min()
    minpetalwidth = df['petal_width'].min()

    # Print Min, Max & Median values of each attribute by class to the text file
    print ("Min values for each attribute by Class: ")
    minvalues = df.groupby('class').min()
    print (minvalues)
    print("\n")
    print ("Max values for each attribute by Class: ")
    maxvalues = df.groupby('class').max()
    print (maxvalues)
    print("\n")
    print ("Median values for each attribute by Class: ")
    medianvalues = df.groupby('class').median()
    print (medianvalues)
    print("\n")
    print ("Mode of each attribute: ")

    # Print the mode but only for the four measurement columns (not the index or class column)
    modevalues = df.mode(axis=0,numeric_only=True,dropna=True) # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mode.html
    print (modevalues)
    print("\n")

    # Print out min/max value for each attribute & corresponding index position and class of flower
    # This will provide some more meaningful analysis & will help to distinguish the classes of flower from each other
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

    # Switching the print output back to the terminal
    sys.stdout = original_stdout # Code copied from: https://stackabuse.com/writing-to-a-file-with-pythons-print-function/
    return print ("Analysis has been completed. Please see file summary.csv")

# Histograms function - this will plot and save a histogram of each variable as a .png file
def histograms():
    file = "dataforproject.csv"
    df = pd.read_csv(file) 
    # Plot histogram for sepal_length
    sns.histplot(df, x="sepal_length", bins=30, hue="class") # the value for bins was decided through trial and error, 30 looked good to me!
    plt.xlabel("sepal length (cm)", size=12)
    plt.ylabel("") # leaving the y axis label blank
    plt.title("Histogram of Variable: sepal_length", size=16)
    # Save plot
    plt.savefig("sepal_length_hist.png")
     # Plot histogram for sepal_width
    sns.histplot(df, x="sepal_width", bins=30, hue="class")
    plt.xlabel("sepal width (cm)", size=12)
    plt.ylabel("") # leaving the y axis label blank
    plt.title("Histogram of Variable: sepal_width", size=16)
    # Save plot
    plt.savefig("sepal_width_hist.png")
      # Plot histogram for petal_length
    sns.histplot(df, x="petal_length", bins=30, hue="class")
    plt.xlabel("petal length (cm)", size=12)
    plt.ylabel("") # leaving the y axis label blank
    plt.title("Histogram of Variable: petal_length", size=16)
    # Save plot
    plt.savefig("petal_length_hist.png")
    # Plot histogram for petal_width
    sns.histplot(df, x="petal_width", bins=30, hue="class")
    plt.xlabel("petal width (cm)", size=12)
    plt.ylabel("") # leaving the y axis label blank
    plt.title("Histogram of Variable: petal_width", size=16)
    # Save plot
    plt.savefig("petal_width_hist.png")

    return print ("A histogram of each variable has been saved to the local folder as a .png file")

# Scatterplots function - this will plot and save a scatterplot for all pairs of variables
# The project instructions did not specify if the scatterplots needed to be on separate files, so I went with the PairGrid approach
def scatterplots():
    file = "dataforproject.csv"
    # Creating a list of the variables I want to use in the scatterplots (as I don't want to use index & class):
    variables = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    df = pd.read_csv(file) 
    sns.set_style("ticks") # changing the theme to ticks
    g = sns.PairGrid(df, hue="class", vars=variables) # adapted from: https://seaborn.pydata.org/generated/seaborn.PairGrid.html
    g.map(sns.scatterplot)
    g.add_legend()
    # Code in loop below copied from: https://stackoverflow.com/questions/30921164/seaborn-pairgrid-show-axes-tick-labels-for-each-subplot
    for ax in g.axes.flat:
        _ = plt.setp(ax.get_yticklabels(), visible=True)
        _ = plt.setp(ax.get_xticklabels(), visible=True)
    plt.savefig("scatter_plots.png")

    return print ("A scatter plot of each pair of variables has been saved. See scatter_plots.png")

summary()
histograms()
scatterplots()