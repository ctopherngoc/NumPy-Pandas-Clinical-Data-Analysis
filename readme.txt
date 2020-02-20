Assignment 5
Author: Christopher Nguyen

How to run:
1. Must have following files in the same directory:
    Week10.py
    clinical_data.txt
    distanceFiles Directory 
    diversityScores Directory
4. Run week10.py

Week10.py utilizes the NumPy and Pandas Python libraries to open up the clinical_data.txt file in a dataframe. It searches for the code_name column and appends them into a list. This list is utilized to open up each diversity score and distance file through a loop. It begins by opening each code_name distance.txt located in the distanceFiles directory. It calculates the mean and the standard deviation for each code_name then appends it into the original dataframe under the mean and STD columns. This modified dataframe is then outputted as clinical_data.stats.txt.

The program thens sorts the dataframe from lowest to highest mean. It appends the lowest and two highest mean code_name into a list. This list is utilized to open up the three code_name distance.txt located within the distanceFiles directory. The .txt file are then utilized to plot a scatter plot and is outputted as a PNG file in the root directory where week10.py is located.   