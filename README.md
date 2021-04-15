# pands-project2021
**Author:** Gillian Kane-McLoughlin

ReadMe file for my Project for the Programming & Scripting module.

**Summary:**  
Fisher’s Iris dataset contains records on the length and width measurements for the Iris flower dataset of the following three Irish species: Iris setosa, Iris virginica, and Iris versicolor.  
It was created by Sir Ronald Aylmer Fisher, a statistician and geneticist, and was first published in a report in 1936 entitled “The Use of Multiple Measurements in Taxonomic Problems” in the journal Annals of Eugenics.  
Fisher used a linear function to differentiate between the three different Iris species based on the morphology of their flowers. 150 samples are contained in the data set, and the measurements were taken in centimetres.  
Records were recorded under 5 attributes - Petal Length, Petal Width, Sepal Length, Sepal Width and Class(Species).  
The data set is also known as Anderson's Iris data set, as the data was collected by Edgar Anderson and not Fischer himself, as well as the Iris flower dataset.  


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

**Data Source:**  https://archive.ics.uci.edu/ml/datasets/iris 

**References:**  
https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d  
https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342  
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html  
http://rstudio-pubs-static.s3.amazonaws.com/450733_9a472ce9632f4ffbb2d6175aaaee5be6.html 
https://stackabuse.com/writing-to-a-file-with-pythons-print-function/   
https://stackoverflow.com/questions/17071871/how-to-select-rows-from-a-dataframe-based-on-column-values  
https://stackoverflow.com/questions/26063231/read-specific-columns-with-pandas-or-other-python-module  
https://stackoverflow.com/questions/31037298/pandas-get-column-average-mean
https://stackoverflow.com/questions/36684013/extract-column-value-based-on-another-column-pandas-dataframe  
https://stackoverflow.com/questions/60305914/reading-data-files-using-pandas  
https://subscription.packtpub.com/book/big_data_and_business_intelligence/9781787286382/1/ch01lvl1sec13/viewing-the-iris-dataset-with-pandas  
https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5  
http://www.cse.msu.edu/~ptan/dmbook/tutorials/tutorial3/tutorial3.html  
https://www.datacamp.com/community/tutorials/python-select-columns  
https://www.geeksforgeeks.org/python-pandas-dataframe-describe-method/  
https://www.kaggle.com/arshid/iris-flower-dataset  
https://www.kite.com/python/answers/how-to-add-a-header-to-a-csv-file-in-python# 
http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html  
https://www.learnbay.co/data-science-course/blog-post/exploratory-data-analysis-on-iris-dataset/   
https://www.w3resource.com/python-exercises/csv/python-csv-exercise-7.php  






