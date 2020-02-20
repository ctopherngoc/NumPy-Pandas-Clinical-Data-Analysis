import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#Create relative paths and absolute paths for directories
script_dir = os.path.dirname(__file__)
rel_path_scores = "diversityScores/"
rel_path_distance = "distanceFiles/"
abs_file_path_scores = os.path.join(script_dir, rel_path_scores)
abs_file_path_distance = os.path.join(script_dir, rel_path_distance)


#Open clinical_Data.txt, extract code_names, and create lists for parsing
df = pd.read_csv('clinical_data.txt', delimiter = '\t')
result = df["code_name"].tolist()
averages = []
stds = []
max = []
min = []

####################################
#for loop to calculate and append mean and standard deviation for each code_name to list
for i in result:
    dx = pd.read_csv(abs_file_path_scores + i + ".diversity.txt", header = None)
    dx.columns = ['Number']
    #print(dx)
    averages.append(dx['Number'].mean())
    stds.append(dx['Number'].std())


####################################
#add mean and standard deviation to dataframe
df['Mean'] = averages
df['STD'] = stds

#sort dataframe lowest to highest mean
df.sort_values(by=['Mean'])


#output dataframe as new text file
df.to_csv(script_dir + '/clinical_data.stats.txt', sep='\t', index=False)

####################################

#create list containing the code_names for the two highest and lowest mean average
scatter_list = []
scatter_list.append((df.sort_values(by=['Mean']).iloc[0]['code_name']))
scatter_list.append((df.sort_values(by=['Mean']).iloc[-1]['code_name']))
scatter_list.append((df.sort_values(by=['Mean']).iloc[-2]['code_name']))

#Loop to open up dataframe of each code_name.distance.txt, create scatter plot and save as code_name.png
for i in scatter_list:
    dc = pd.read_csv(abs_file_path_distance + i + ".distance.txt", header=None)
    dc.columns = ['x','y']

    plot = dc.plot(kind = 'scatter', x='x', y='y', c='DarkBlue', title = i)
    plot.figure.savefig(i+'_scatterplot.png')