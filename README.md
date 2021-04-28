# pands-project2021
**Author:** Gillian Kane-McLoughlin  
**Student Number:** G00398258  

This is the ReadMe file for my Final Project for the Programming & Scripting module, completed in April 2021.  

# **Summary:**  
Fisher’s Iris dataset contains records on the length and width measurements of flowers from the following three Iris species: Iris Setosa, Iris Virginica, and Iris Versicolor.  

![image](https://github.com/G00398258/pands-project2021/blob/main/flowers.png)  
*Image Source: Ref [1]*  

The dataset was created by Sir Ronald Aylmer Fisher, a statistician and geneticist, and was first published in a report in 1936 entitled “The Use of Multiple Measurements in Taxonomic Problems” in the journal Annals of Eugenics.  
The dataset is sometimes referred to as Anderson's Iris dataset, as the data was collected by Edgar Anderson and not Fisher himself, and is also known as the Iris flower dataset.  
Fisher used a linear function to differentiate between the three different Iris species mentioned above based on the morphology of their flowers. 150 samples are contained in the dataset, 50 from each of the three different species and the measurements were taken in centimetres.  
The data was recorded under 4 measurement attributes - Petal Length, Petal Width, Sepal Length and Sepal Width - as well as by the Class (or Species) of flower.    
*Refs: [3],[4],[7],[20],[22]*  

# **Data Source & Software Information:**  
The dataset used in this project was downloaded from: https://archive.ics.uci.edu/ml/datasets/iris  
The code for this project was written in Python and ran in Visual Studio Code, Version 1.55.2

# **What does this Program Do?**  
The aim of this program is to attempt to identify the different classes of flower from each other using the data provied in the Iris dataset.  

The program begins by importing the following modules:   
*import matplotlib.pyplot as plt*  
*import pandas as pd*  
*import sys*  
*import shutil*  
*import seaborn as sns*  

Using the shutil module, the program copies the data on the iris.data file to a new file named dataforproject.csv and creates a dataframe that reads in this data (*note:* this was done as I ran the program several times over the course of completing the project, and wanted to be able to use the raw data file rather than the version of the file my code goes onto create, so anyone can run the code in the same way).  
The program adds the following column names to the new file: "sepal_length", "sepal_width", "petal_length", "petal_width", "class".  
3 functions are then called by the program: summary(), histograms() & scatterplots()  

- **Summary Function**  
The summary() function uses the sys module to change the standard output destination to a new file called summary.txt. It creates a dataframe by reading in the data on the dataforproject.csv file and adds an index, to avoid any issues with unnamed columns.  
It then writes some general statistics to the summary.txt file using the following functions: 

- describe(): produces statistics such as the count, mean, standard deviation, etc. for each variable  
- head(5): prints the first 5 rows of the dataset     
- tail(5): prints the last 5 rows of the dataset    
- shape(): describes the shape of the dataset in terms of rows and columns    
- value_counts(): lists the number of values per attribute (in this case, "class")      
- cov(): details the covariance between the attributes    
- corr(): details the correlation between the attributes    

The function then produces the min, max, and median values of each attribute by class, and the mode of the four measurement attributes.  
Finally, the function prints out the min & max value for each attribute & the corresponding index position and class of flower for that value.  

The sys module is called again to reset the standard output destination to the terminal.  
The function returns "Analysis has been completed. Please see file summary.csv" when it has finished running.  

- **Histograms Function**  
The histograms() function also creates a dataframe by reading in the data on the dataforproject.csv file.  
Using the seaborn & matplotlib modules, it plots a separate histogram for Sepal Length, Sepal Width, Petal Length & Petal Width using the hue "class", applies a legend and saves them as follows: 
 
- sepal_length_hist.png  
![image](https://github.com/G00398258/pands-project2021/blob/main/sepal_length_hist.png)    
- sepal_width_hist.png  
![image](https://github.com/G00398258/pands-project2021/blob/main/sepal_width_hist.png)   
- petal_length_hist.png  
![image](https://github.com/G00398258/pands-project2021/blob/main/petal_length_hist.png)  
- petal_width_hist.png  
![image](https://github.com/G00398258/pands-project2021/blob/main/petal_width_hist.png)  

The function returns "A histogram of each variable has been saved to the local folder as a .png file" when it has finished running.

- **Scatterplots Function**  
The scatterplots() function again creates a dataframe by reading in the data on the dataforproject.csv file.  
It defines the variables to use in the scatterplots in a list (Sepal Length, Sepal Width, Petal Length & Petal Width) as the index and class will not be required.    
As the project instructions did not specify if we needed to save an individual .png file for each scatterplot, I chose to use the PairGrid approach to produce one file with all of the scatterplots after discovering the function in the course of my research.   

Using the seaborn module & the PairGrid function, the program plots a scatter plot for each pair of variables (16 plots in total) on one .png file, applies labels, titles, and saves the below file as scatter_plots.png:  
![image](https://github.com/G00398258/pands-project2021/blob/main/scatter_plots.png)  
The function returns "A scatter plot of each pair of variables has been saved. See scatter_plots.png" when it has finished running. 
The above line is the last output of my code.   

# **Conclusion**
The analysis outputted to the summary.txt file (particularly the identification of the class of flower with the largest/smallest attributes) combined with the visuals of the plots produced by the code should help us to differentiate between the different species of flower recorded in the dataset.

Based on the results of this analysis, I have concluded the following:  
With the exception of the measurements of Sepal Width, my analysis showed that the species Iris Virginica contained the flowers with the largest attribute measurements while the species Iris Setosa contained the flowers with the smallest, thus allowing us to differentiate between the classes of flower based on the measurements of Sepal Length, Petal Length & Petal Width.  


# **References:**  
Please note that any code copied directly from another source has been referenced in my code.  
The below list of references includes any such cases, as well as all other sources engaged with or researched in the course of completing this project.  
 
1) https://datascience-enthusiast.com/R/Simpson_paradox.html  
2) https://datavizpyr.com/change-axis-labels-set-title-and-figure-size-to-plots-with-seaborn/  
3) https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d  
4) https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342  
5) https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mode.html  
6) https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html  
7) https://pythonhosted.org/bob/temp/bob.db.iris/doc/example.html  
8) http://rstudio-pubs-static.s3.amazonaws.com/450733_9a472ce9632f4ffbb2d6175aaaee5be6.html 
9) https://seaborn.pydata.org/generated/seaborn.histplot.html  
10) https://seaborn.pydata.org/generated/seaborn.PairGrid.html  
11) https://seaborn.pydata.org/introduction.html  
12) https://stackabuse.com/how-to-copy-a-file-in-python/  
13) https://stackabuse.com/writing-to-a-file-with-pythons-print-function/   
14) https://stackoverflow.com/questions/17071871/how-to-select-rows-from-a-dataframe-based-on-column-values  
15) https://stackoverflow.com/questions/26063231/read-specific-columns-with-pandas-or-other-python-module  
16) https://stackoverflow.com/questions/30921164/seaborn-pairgrid-show-axes-tick-labels-for-each-subplot  
17) https://stackoverflow.com/questions/31037298/pandas-get-column-average-mean
18) https://stackoverflow.com/questions/36684013/extract-column-value-based-on-another-column-pandas-dataframe  
19) https://stackoverflow.com/questions/60305914/reading-data-files-using-pandas  
20) https://towardsdatascience.com/eda-of-the-iris-dataset-190f6dfd946d  
21) https://subscription.packtpub.com/book/big_data_and_business_intelligence/9781787286382/1/ch01lvl1sec13/viewing-the-iris-dataset-with-pandas  
22) https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5  
23) http://www.cse.msu.edu/~ptan/dmbook/tutorials/tutorial3/tutorial3.html  
24) https://www.datacamp.com/community/tutorials/python-select-columns  
25) https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/  
26) https://www.geeksforgeeks.org/python-pandas-dataframe-describe-method/  
27) https://www.geeksforgeeks.org/python-pandas-dataframe-mode/#:~:text=mode()%20function%20gets%20the,why%20a%20dataframe%20is%20returned.  
28) https://www.kaggle.com/arshid/iris-flower-dataset  
29) https://www.kaggle.com/noelano/seaborn-visualization-on-iris-data-set  
30) https://www.kite.com/python/answers/how-to-add-a-header-to-a-csv-file-in-python# 
31) http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html  
32) https://www.learnbay.co/data-science-course/blog-post/exploratory-data-analysis-on-iris-dataset/   
33) https://www.w3resource.com/python-exercises/csv/python-csv-exercise-7.php  









