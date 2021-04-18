import numpy as n
import matplotlib.pyplot as plt
import pandas as pd
import sys
import shutil
import seaborn as sns

file = "dataforproject.csv"
# Copying data from raw dataset to a new file, as I will be adding columns names and an index later on
shutil.copyfile("iris.data", "dataforproject.csv") # https://stackabuse.com/how-to-copy-a-file-in-python/

df = pd.read_csv(file, header=None) 
# Adding column names on the csv file
df.to_csv(file, header=["sepal_length", "sepal_width", "petal_length", "petal_width", "class"])

# Summary function
def summary():
    file = "dataforproject.csv"
    original_stdout = sys.stdout # https://stackabuse.com/writing-to-a-file-with-pythons-print-function/
    # reading in the data within the function & setting the index column so I don't get an unnamed column in my output (lecture on pandas helped here!)
    df = pd.read_csv(file, index_col=0) 
    f = open("summary.csv", "a")
    sys.stdout = f # this will output print commands to the analysis.csv file (f)

    # General summary points: describe, head, tail, shape, value counts, covairance & correlation 
    print ("General Statistics: \n", df.describe())
    print("\n") # adding an empty line between each data point to make it look and read a bit better
    print ("First 5 Rows: \n", df.head(5))
    print("\n")
    print ("Last 5 Rows: \n", df.tail(5))
    print("\n")
    print ("Shape of Dataset (# rows, # columns): ", df.shape)
    print("\n")
    print ("Value Counts for each Class: \n",df["class"].value_counts())
    print("\n")
    print("Covariance: \n", df.cov())
    print("\n")
    print("Correlation: \n", df.corr()) 
    print("\n")
    '''I was going to have the program print out the dataset by each class, but decided this would be a bit overkill
    print ("Dataset for Class: Iris-setosa")
    print (df.loc[df["class"] == "Iris-setosa"])
    print("\n")
    print ("Dataset for Class: Iris-versicolor")
    print (df.loc[df["class"] == "Iris-versicolor"])
    print("\n")
    print ("Dataset for Class: Iris-virginica")
    print (df.loc[df["class"] == "Iris-virginica"])
    print("\n")
    '''
    


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

    # More specific analysis
    # Min, Max & Median values of each attribute by class
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
    modevalues = df.mode(axis=0,numeric_only=True,dropna=True) # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mode.html
    print (modevalues)
    print("\n")

    # Print out min/max value for each attribute & correspoting index position and class of flower
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

    sys.stdout = original_stdout # switching the print output back to the terminal
    return print ("Analysis has been completed. Please see file summary.csv")

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
summary()

def histograms():
    file = "dataforproject.csv"
    variables = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
    df = pd.read_csv(file) 
    # Plot histogram for sepal_length
    sns.histplot(df, x="sepal_length", bins=30, hue="class")
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
    
    '''sns.histplot(data=iris, x="sepal_length",hue="species")
    iris = sns.load_dataset("iris")
    sns.histplot(data=iris, x="sepal_width")
    iris = sns.load_dataset("iris")
    sns.histplot(data=iris, x="petal_length")
    iris = sns.load_dataset("iris")
    sns.histplot(data=iris, x="petal_width")'''
    
    #g = sns.PairGrid(iris, hue="species")
    #.map_diag(sns.histplot)
    #g.map_offdiag(sns.scatterplot)
    #g.add_legend()
    return print ("A histogram of each variable has been saved.")

def scatterplots():
    file = "dataforproject.csv"
    variables = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    df = pd.read_csv(file) 
    g = sns.PairGrid(df, hue="class", vars=variables, height=3)
    g.map(sns.scatterplot)
    g.add_legend()
    plt.savefig("scatter_plots.png")
    return print ("A scatter plot of each pair of variables has been saved. See scatter_plots.png")

histograms()
scatterplots()