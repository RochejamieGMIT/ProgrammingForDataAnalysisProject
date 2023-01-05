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
                         names=['id number', 'Clump Thickness', 'Uniformity of Cell Size', ' Uniformity of Cell Shape','Marginal Adhesion','Single Epithelial Cell Size','Bare Nuclei','Bland Chromatin','Normal Nucleoli','Mitoses','Class'])


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


#print(df)