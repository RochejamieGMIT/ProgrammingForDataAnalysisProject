# ProgrammingForDataAnalysisProject

This is a project to investigate the Breast Cancer Wisconsin (Original) Data Set.

The project starts with a brief introduction to the data set. 

Next a literary review of some existing papers about the data set. 

Paper 1 - Analysis of the Wisconsin Breast Cancer Dataset and Machine Learning for Breast Cancer Detection
by Borges, Lucas Rodrigues
https://www.researchgate.net/profile/Lucas-Borges-13/publication/311950799_Analysis_of_the_Wisconsin_Breast_Cancer_Dataset_and_Machine_Learning_for_Breast_Cancer_Detection/links/5864757e08ae329d6203aa82/Analysis-of-the-Wisconsin-Breast-Cancer-Dataset-and-Machine-Learning-for-Breast-Cancer-Detection.pdf

Paper 2 - ANALYSIS OF FEATURE SELECTION WITH CLASSFICATION: BREAST CANCER DATASETS
by D.Lavanya and Dr.K.Usha Rani
http://ijcse.com/docs/INDJCSE11-02-05-167.pdf

Paper 3 - Analysis of Wisconsin Breast Cancer original dataset using data mining and machine learning algorithms for breast cancer prediction
by Md. Toukir Ahmed, Md. Niaz Imtiaz and Animesh Karmakar
https://www.journalbinet.com/uploads/2/1/0/0/21005390/67.02.09.2020_analysis_of_wisconsin_breast_cancer_original_dataset_using_data_mining_and_machine_learning_algorithms_for_breast_cancer_prediction.pdf

Next, the data was analysed. 

First, I created a Pie chart to show the number of the benign V malignant results. 
I also created a heat map to see how the values of the attributes correlate. 
Most notable being that mitoses did not correlate strongly with other attributes, including the class.

Next I used box plots for each attribute, plotting the attribute against the class to see how the benign and malignant values are distributed. 

Next, I split the data frame in to 2 sections, one benign and one malignant to print out a summary of the data’s in their classes, to get Max, Min, Median and mean for each attribute. 

Next I used the split data to create overlaying histograms of the benign data and the malignant data per attribute to further  visualize how these are distributed. 

Then I wrote a brief summary of the data and graphs above. 

Next I tried to classify the data, I used three methods. 

Nearest Neighbour, Naive Bayesian and J48 (Decision Tree). 

Entering into classification I expected Bayesian to out perform J48, as that was a trend in the research. 
Nearest neighbour was surprising in that the classification was more accurate than initially expected. 
Nearest neighbour, over multiple test was able to match the accuracy of Naive Bayesian of 96 - 97% on multiple runs. 

I then wrote a brief summary of the parameters used, followed by a compare and contrast of the results. 

Then finally there was an attempt to synthesis data. I was able to recreate the classification ratio relatively accurately, but the individual values did not correlate to each other accurately. This is because generated each value individually using the weightings of the frequency that values appeared in the original data for the attributes. Then I used the nearest neighbour classifier to create the class column for the data. 

With more time, I could apply the same weightings per attribute based on the previous result of generated attribute. 
This could be tedious with nested else if statements, but in theory could give more accurate results. or at least results that would appear to be more accurate to the original data.

if the attributes were ranked in highest correlation and then the highest correlated values were generated in succession and had the frequencies specific to the previous generated value be the weights of the next value to be generated that could be a way to synthesis data. 


References: 
As a note, I have relied on code I have written in previous modules, particularly code for the pands project:
https://github.com/RochejamieGMIT/pands-project


https://archive.ics.uci.edu/ml/datasets/breast+cancer+wisconsin+(original)
http://odds.cs.stonybrook.edu/breast-cancer-wisconsin-original-dataset/
https://www.researchgate.net/profile/Lucas-Borges-13/publication/311950799_Analysis_of_the_Wisconsin_Breast_Cancer_Dataset_and_Machine_Learning_for_Breast_Cancer_Detection/links/5864757e08ae329d6203aa82/Analysis-of-the-Wisconsin-Breast-Cancer-Dataset-and-Machine-Learning-for-Breast-Cancer-Detection.pdf
https://www.sciencedirect.com/topics/mathematics/bayesian-network#:~:text=and%20Markov%20models-,A%20Bayesian%20network%20(BN)%20is%20a%20probabilistic%20graphical%20model%20for,belief%20networks%20or%20Bayes%20nets.
http://www.malinc.se/math/latex/basiccodeen.php#:~:text=To%20write%20a%20fraction%2C%20you,in%20text%20are%20called%20inline.
https://tex.stackexchange.com/questions/400108/how-to-put-vertical-line-among-the-words
https://www.geeksforgeeks.org/building-a-machine-learning-model-using-j48-classifier/
https://medium.com/@nilimakhanna1/j48-classification-c4-5-algorithm-in-a-nutshell-24c50d20658e
http://ijcse.com/docs/INDJCSE11-02-05-167.pdf
https://www.geeksforgeeks.org/cart-classification-and-regression-tree-in-machine-learning/
https://www.javatpoint.com/principal-component-analysis
https://stackoverflow.com/questions/12298150/what-is-the-difference-between-a-bayesian-network-and-a-naive-bayes-classifier
https://stats.stackexchange.com/questions/212240/the-difference-between-the-bayes-classifier-and-the-naive-bayes-classifier#:~:text=Naive%20Bayes%20assumes%20conditional%20independence,%2C%20in%20fact%2C%20conditionally%20independent.
https://stackoverflow.com/questions/12298150/what-is-the-difference-between-a-bayesian-network-and-a-naive-bayes-classifier
https://towardsdatascience.com/a-beginners-guide-to-data-analysis-in-python-188706df5447
https://plotly.com/python/renderers/
https://www.geeksforgeeks.org/python-pandas-dataframe-isin/
https://stackoverflow.com/questions/34844711/convert-entire-pandas-dataframe-to-integers-in-pandas-0-17-0
https://www.datasciencelearner.com/pd-to_numeric-method-pandas-dataframe/
https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/06_calculate_statistics.html
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.agg.html#pandas.DataFrame.agg
https://plotly.com/python/histograms/
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html
https://scikit-learn.org/stable/modules/naive_bayes.html
https://scikit-learn.org/stable/modules/tree.html
https://stackoverflow.com/questions/53987391/transform-from-one-decision-tree-j48-classification-to-ensemble-in-python
https://sparkbyexamples.com/pandas/pandas-count-frequency-value-occurs-in-dataframe-column/#:~:text=In%20pandas%20you%20can%20get,()%20and%20count()%20method.
https://pythonexamples.org/pandas-dataframe-add-append-row/
https://stackoverflow.com/questions/70837397/good-alternative-to-pandas-append-method-now-that-it-is-being-deprecated