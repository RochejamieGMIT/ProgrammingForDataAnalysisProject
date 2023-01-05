import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import pandas_profiling as pp
import plotly.graph_objs as go
import plotly.tools as tls
import plotly.express as px
import numpy as np


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data"

#Importing data set from url, Adding Headings for ease of viewing 
df = pd.read_csv(url, sep='\,',
                         names=['id number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape','Marginal Adhesion','Single Epithelial Cell Size','Bare Nuclei','Bland Chromatin','Normal Nucleoli','Mitoses','Class'])


#https://stackoverflow.com/questions/52553062/pandas-profiling-doesnt-display-the-output
#report = pp.ProfileReport(df)
#report.to_file('profile_report.html') # To preview data had to create a .html file as vs code could not open it

# Reference for the Pi chart 
# https://towardsdatascience.com/a-beginners-guide-to-data-analysis-in-python-188706df5447
dist = df['Class'].value_counts()
trace = go.Pie(values=(np.array(dist)),labels=['Benign','Malignant'])
layout = go.Layout(title='Class Distribution')
data = [trace]
fig = go.Figure(trace,layout)
fig.write_image("Pie_ValueCountCheck.png") # Generating a pie chart to compare the percentage of Benign V Malignant

def df_to_plotly(df):
    return {'z': df.values.tolist(),
            'x': df.columns.tolist(),
            'y': df.index.tolist() }
dfNew = df.corr() # Compute pairwise correlation with another DataFrame or Series.
fig = go.Figure(data=go.Heatmap(df_to_plotly(dfNew))) #Creates a heatmap of the data to check for correlations 
fig.write_image("Heatmap.png") # The Values mostly appeear to have high correlation, appart from ID number, Which is not related
# to the vaules, so that is expected. Also, Mitoses is the value that has the lowest correlation to other values 

# https://plotly.com/python/renderers/
# https://plotly.com/python/static-image-export/
#
fig = px.scatter(df, x='Clump Thickness', y='Class') # create a scatter plot of 
fig.update_traces()
fig.update_layout(title_text='Clump Thickness and Class') # Add title
fig.write_image("Clump Thickness.png") # Save to PNG
# I found this interesting as putting each Class side by side you can see where they over lap

fig = px.scatter(df, x='Uniformity of Cell Size', y='Class') # create a scatter plot of 
fig.update_traces()
fig.update_layout(title_text='Uniformity of Cell Size and Class') # Add title
fig.write_image("Uniformity of Cell Size.png") # Save to PNG
# I found this interesting as putting each Class side by side you can see where they over lap

fig = px.box(df, x='Class', y='Clump Thickness') #Creates a box graph of petal length for each class
fig.update_traces
fig.update_layout(title_text='class and Clump Thickness') # title
fig.write_image("Box1_Clump_Thickness.png") # save to png

fig = px.box(df, x='Class', y='Uniformity of Cell Size') #Creates a box graph of petal length for each class
fig.update_traces
fig.update_layout(title_text='class and Uniformity of Cell Sizes') # title
fig.write_image("Box2_Uniformity_of_Cell_Size.png") # save to png

fig = px.box(df, x='Class', y='Uniformity of Cell Shape') #Creates a box graph of petal length for each class
fig.update_traces
fig.update_layout(title_text='class and Uniformity of Cell Shape') # title
fig.write_image("Box3_Uniformity_of_Cell_Shape.png") # save to png

fig = px.box(df, x='Class', y='Marginal Adhesion') #Creates a box graph of petal length for each class
fig.update_traces
fig.update_layout(title_text='class and Marginal Adhesion') # title
fig.write_image("Box4_Marginal_Adhesion.png") # save to png


fig = px.box(df, x='Class', y='Single Epithelial Cell Size') #Creates a box graph of petal length for each class
fig.update_traces
fig.update_layout(title_text='class and Single Epithelial Cell Size') # title
fig.write_image("Box5_Single_Epithelial.png") # save to png

fig = px.box(df, x='Class', y='Bare Nuclei') #Creates a box graph of petal length for each class
fig.update_traces
fig.update_layout(title_text='class and Bare Nuclei') # title
fig.write_image("Box6_Bare_Nuclei.png") # save to png

fig = px.box(df, x='Class', y='Bland Chromatin') #Creates a box graph of petal length for each class
fig.update_traces
fig.update_layout(title_text='class and Bland Chromatin') # title
fig.write_image("Box7_Bland_Chromatin.png") # save to png

fig = px.box(df, x='Class', y='Normal Nucleoli') #Creates a box graph of petal length for each class
fig.update_traces
fig.update_layout(title_text='class and Normal Nucleoli') # title
fig.write_image("Box8_Normal_Nucleoli.png") # save to png

fig = px.box(df, x='Class', y='Mitoses') #Creates a box graph of petal length for each class
fig.update_traces
fig.update_layout(title_text='class and Mitoses') # title
fig.write_image("Box9_Mitoses.png") # save to png

print(df)
# seperating each species to their own group using isin function
# https://www.geeksforgeeks.org/python-pandas-dataframe-isin/
BenignGroup = df[df["Class"].isin([2])]
BenignGroup = BenignGroup.drop(BenignGroup.columns[0], axis=1)

BenignGroup = BenignGroup.apply(pd.to_numeric, errors='coerce')


print(BenignGroup)
# remove unwanted column of identifying numbers // https://stackoverflow.com/questions/39399712/delete-pandas-column-with-no-name

MalignantGroup = df[df["Class"].isin([4])]
MalignantGroup = MalignantGroup.drop(MalignantGroup.columns[0], axis=1)
# https://www.datasciencelearner.com/pd-to_numeric-method-pandas-dataframe/ avoid ? character in Bare Nuclei
# https://stackoverflow.com/questions/34844711/convert-entire-pandas-dataframe-to-integers-in-pandas-0-17-0
# How to user pd.to_numeric with a dataframe

MalignantGroup = MalignantGroup.apply(pd.to_numeric, errors='coerce')
print(MalignantGroup)

# https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/06_calculate_statistics.html
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.agg.html#pandas.DataFrame.agg
#
#Summarise the data in each class 
#Initially the bare Nucleoli is not displaying in the summary correctly. 

SumBenign = BenignGroup.agg(
    {
        "Clump Thickness" : ["min", "max", "median","mean"],
        "Uniformity of Cell Size" : ["min", "max", "median","mean"],
        "Uniformity of Cell Shape" : ["min", "max", "median","mean"],
        "Marginal Adhesion" : ["min", "max", "median","mean"],
        "Single Epithelial Cell Size" : ["min", "max", "median","mean"],
        "Bare Nuclei" : ["min", "max", "median","mean"],
        "Bland Chromatin" : ["min", "max", "median","mean"],
        "Normal Nucleoli" : ["min", "max", "median","mean"],
        "Mitoses" : ["min", "max", "median","mean"]
    }
)


SumMalignat= MalignantGroup.agg(
    {
        "Clump Thickness" : ["min", "max", "median","mean"],
        "Uniformity of Cell Size" : ["min", "max", "median","mean"],
        "Uniformity of Cell Shape" : ["min", "max", "median","mean"],
        "Marginal Adhesion" : ["min", "max", "median","mean"],
        "Single Epithelial Cell Size" : ["min", "max", "median","mean"],
        "Bare Nuclei" : ["min", "max", "median","mean"],
        "Bland Chromatin" : ["min", "max", "median","mean"],
        "Normal Nucleoli" : ["min", "max", "median","mean"],
        "Mitoses" : ["min", "max", "median","mean"]
    }
)

BareNuclei = df["Bare Nuclei"]

with open('summary.txt', 'a') as f:
    f.write("\nThis is a summary of the breast cancer databases that was obtained from the University of Wisconsin Hospitals \n Overall data set information:\n")
    df.info(buf=f)#Writing the sys.stdout to file https://stackoverflow.com/questions/35436331/how-to-save-output-from-dataframe-info-to-file-a-excel-or-text-file
    f.write("\nThe summary for the benign results are as follows: \n")
    dfAsString = SumBenign.to_string(header=True, index=True) # https://stackoverflow.com/questions/31247198/python-pandas-write-content-of-dataframe-into-text-file
    f.write(dfAsString)
    f.write("\nThe summary for the malignat results are as follows: \n")
    dfAsString = SumMalignat.to_string(header=True, index=True)
    f.write(dfAsString)

    f.write("\n Bare Nuclei is not working correctly, I am going to add it to the summary .txt to look in to it \n")
    dfAsString = BareNuclei.to_string(header=True, index=True)
    f.write(dfAsString)
f.close()





#print(df)