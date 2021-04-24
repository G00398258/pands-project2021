# pands-project2021
**Author:** Gillian Kane-McLoughlin

ReadMe file for my Project for the Programming & Scripting module.

**Summary:**  
Fisher’s Iris dataset contains records on the length and width measurements for the Iris flower dataset of the following three Irish species: Iris setosa, Iris virginica, and Iris versicolor.  
It was created by Sir Ronald Aylmer Fisher, a statistician and geneticist, and was first published in a report in 1936 entitled “The Use of Multiple Measurements in Taxonomic Problems” in the journal Annals of Eugenics.  
Fisher used a linear function to differentiate between the three different Iris species based on the morphology of their flowers. 150 samples are contained in the data set, and the measurements were taken in centimetres.  
Records were recorded under 5 attributes - Petal Length, Petal Width, Sepal Length, Sepal Width and Class(Species).  
The data set is also known as Anderson's Iris data set, as the data was collected by Edgar Anderson and not Fischer himself, as well as the Iris flower dataset.  

**Data Source:**  
The dataset used in this project was downloaded from: https://archive.ics.uci.edu/ml/datasets/iris  

**What does this Program Do?**  
The program begins by importing the following modules:  
import numpy as n  
import matplotlib.pyplot as plt  
import pandas as pd  
import sys  
import shutil  
import seaborn as sns  

Using the shutil module, it then copies the data on the iris.data file to a new file named dataforproject.csv and creates a dataframe that reads in this data.  
The program then adds the following column names to the new file: "sepal_length", "sepal_width", "petal_length", "petal_width", "class".  
3 functions are then called by the program: summary(), histograms() & scatterplots()

- **Summary Function**  
The summary() function uses the sys module to change the standard output destination to a new file called summary.csv. It creates a dataframe by reading in the data on the dataforproject.csv file and adds an index.  
It then writes some general statistics to the summary.csv file using the following functions: 
- describe(): produces statistics such as the count, mean, standard deviation, etc. for each variable  
- head(): prints the first 5 rows of the dataset     
- tail(): prints the last 5 rows of the dataset    
- shape(): describes the shape of the dataset in terms or rows and columns    
- value_counts(): lists the number of values per attribute (in this case "class")      
- cov(): details the covariance between the attributes    
- corr(): details the correlation between the attributes    

The function then produces the min, max, and median values of each attribute by class, and the mode of the four measurement attributes.  
Finally, the function prints out the min & max value for each attribute & corresponding index position and class of flower for that value.  
The sys module is called again to reset the standard output destination to the terminal.  
The function returns "Analysis has been completed. Please see file summary.csv" when it has finished running.  

- **Histograms Function**  
The histograms() function creates a dataframe by reading in the data on the dataforproject.csv file.  
Using the seaborn & matplotlib modules, it plots a separate histogram for Sepal Length, Sepal Width, Petal Length & Petal Width using the hue "class", applies a legend and saves them as follows:  
- sepal_length_hist.png  
![image](https://github.com/G00398258/pands-project2021/blob/main/sepal_length_hist.png)    
- sepal_width_hist.png  
![image](https://github.com/G00398258/pands-project2021/blob/main/sepal_width_hist.png)   
- petal_length_hist.png  
![image](https://github.com/G00398258/pands-project2021/blob/main/petal_length_hist.png)  
- petal_width_hist.png  
![image](https://github.com/G00398258/pands-project2021/blob/main/petal_width_hist.png)  
The function returns "A histogram of each variable has been saved" when it has finished running.

- **Scatterplots Function**  
The scatterplots() function also creates a dataframe by reading in the data on the dataforproject.csv file.  
It defines the variables to use in a list (Sepal Length, Sepal Width, Petal Length & Petal Width).   
Using the seaborn module & the PairGrid function, it plots a scatter plot for each pair of variables (16 in total) on one .png file, applies labels, titles, and saves the below file as scatter_plots.png:  
![image](https://github.com/G00398258/pands-project2021/blob/main/scatter_plots.png)  
The function returns "A scatter plot of each pair of variables has been saved. See scatter_plots.png" when it has finished running.  


**Project Progression:**  
To begin with, I spent some time researching how to import the dataset and apply column names to the file I was working with (as these were not on it originally). I learned that I needed to import the pandas module to do this and create a dataframe. I then started researching previous analysis that had been done on the dataset as I tried to decide what exactly I wanted my project to show.  
The general consensus seems to be that the different attributes enable us to distinguish the different species of flower from each other, so I started testing how I could show this in my project.  
I began by using the describe, shape and value counts to produce some basic statistics on the dataset. I then had to do some more research to figure out how I would be able to analyse the data relating to the three individual species of flower, and found I needed to use the "loc" function.  
I'm still really playing with the data and have not produced any plots yet, but I feel I am getting more confortable with the data and should move onto plots in the next few days.  
I'm trying to get my code to print out a line saying something like "The class of flower with the max sepal length is X", but so far I have only managed to use loc to limit the dataframe to rows containing the data for the max sepal length, and can't get it to only print out the class rather than the full row.  
I am doing some more research but think I am spending too much time on this section of the project, and might end up moving on.
I am already producing several data points with my code so it may be best to move onto the plots from here and come back at the end once I have ticked off something for every aspect of this project.  
I have finally gotten my code to print out the class of flower with the min/max of each attribute, mainly thanks to the lecture Andrew posted on Pandas and the https://pandas.pydata.org/ documentation on loc.  
I have moved all of my current code into a function called analysis(), and thanks to https://stackabuse.com/writing-to-a-file-with-pythons-print-function/, I have managed to get the function to write all of the analysis the code is doing to a new file called analysis.csv.  
There is probably too much going on in my analysis at the moment, but I am happy I have gotten to this stage and will be focusing on the plots over the weekend.  
I have now ticked off every requirement for this project.  
I decided to change how my program is reading in the data. The dataset comes in a .data file so instead of me changing the format to .csv and adding the column names & index to this file, I'm now copying the raw file and creating a new file called dataforproject.csv. This saved me a lot of time as prior to this, I had to keep removing the index and column names whenever I ran the program before I could run it again.
I have finished all of the analysis I want to do on the file and have the program outputting this to a file called summary.csv  
I spent some time researching seaborn to see if that might be a better module to use for my plots. I came across the PairGrid & pairplot functions, and I think these could be very useful for the scatter plots required.  
I also used seaborn to create and save four histograms of each attribute.  

**References:**  
Please note that any code copied directly from another source has been referenced in my code.  
The below list of references includes any such cases, as well as all other sources engaged with or researched in the course of completing this project.  
 
https://datavizpyr.com/change-axis-labels-set-title-and-figure-size-to-plots-with-seaborn/  
https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d  
https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342  
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mode.html  
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html  
http://rstudio-pubs-static.s3.amazonaws.com/450733_9a472ce9632f4ffbb2d6175aaaee5be6.html 
https://seaborn.pydata.org/generated/seaborn.histplot.html  
https://seaborn.pydata.org/generated/seaborn.PairGrid.html  
https://seaborn.pydata.org/introduction.html  
https://stackabuse.com/how-to-copy-a-file-in-python/  
https://stackabuse.com/writing-to-a-file-with-pythons-print-function/   
https://stackoverflow.com/questions/17071871/how-to-select-rows-from-a-dataframe-based-on-column-values  
https://stackoverflow.com/questions/26063231/read-specific-columns-with-pandas-or-other-python-module  
https://stackoverflow.com/questions/30921164/seaborn-pairgrid-show-axes-tick-labels-for-each-subplot  
https://stackoverflow.com/questions/31037298/pandas-get-column-average-mean
https://stackoverflow.com/questions/36684013/extract-column-value-based-on-another-column-pandas-dataframe  
https://stackoverflow.com/questions/60305914/reading-data-files-using-pandas  
https://towardsdatascience.com/eda-of-the-iris-dataset-190f6dfd946d  
https://subscription.packtpub.com/book/big_data_and_business_intelligence/9781787286382/1/ch01lvl1sec13/viewing-the-iris-dataset-with-pandas  
https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5  
http://www.cse.msu.edu/~ptan/dmbook/tutorials/tutorial3/tutorial3.html  
https://www.datacamp.com/community/tutorials/python-select-columns  
https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/  
https://www.geeksforgeeks.org/python-pandas-dataframe-describe-method/  
https://www.geeksforgeeks.org/python-pandas-dataframe-mode/#:~:text=mode()%20function%20gets%20the,why%20a%20dataframe%20is%20returned.  
https://www.kaggle.com/arshid/iris-flower-dataset  
https://www.kaggle.com/noelano/seaborn-visualization-on-iris-data-set  
https://www.kite.com/python/answers/how-to-add-a-header-to-a-csv-file-in-python# 
http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html  
https://www.learnbay.co/data-science-course/blog-post/exploratory-data-analysis-on-iris-dataset/   
https://www.w3resource.com/python-exercises/csv/python-csv-exercise-7.php  






