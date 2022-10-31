
# Visualizing survival of plants in an experiment in Norway to see if local plants survive better in their natural environment 
# than plants originating from a southern location.

# First install required packages

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# importing the data file
df = pd.read_csv('AlyrNorway_SpMaF12.txt', delim_whitespace = True)

# examine the column names
print(df.columns)

# For the plot, proportion of plants alive of each population (Sp and NC) need to be calculated separately at each time point:
# after planting outside, after the planting summer (0), after first, second, third and fourth winter and summer (1-4, respectively).


# Columns labeled as "Surv" show if each individual was alive or dead at the time they were surveyed.
# 'Win' shows the situation in the spring and shows after winter survival and 'Sum' refers to end of summer survey.  

# Survival is calculated as proportion of plants alive after planting at each time point, so that the effect of dying right after planting
# can be removed, as it is not natural and can be source of error.

# calculating survival after planting by population group

survivalPla = df.groupby(['Pop'])['SurvPla'].sum() #number of plants alive after a few days after being planted outside

# proportion of plants alive at each time point in each population relative to those alive after planting into a numpy array

survivalNorway = np.array([
    df.groupby(['Pop'])['SurvSum0'].sum()/ survivalPla,    #end of the summer they were planted
    df.groupby(['Pop'])['SurvWin1'].sum()/ survivalPla,    #after first winter
    df.groupby(['Pop'])['SurvSum1'].sum()/ survivalPla,    #after first summer
    df.groupby(['Pop'])['SurvWin2'].sum()/ survivalPla,    #after second winter
    df.groupby(['Pop'])['SurvSum2'].sum()/ survivalPla,    #after second summer
    df.groupby(['Pop'])['SurvWin3'].sum()/ survivalPla,    #after third winter
    df.groupby(['Pop'])['SurvSum3'].sum()/ survivalPla,    #after third summer
    df.groupby(['Pop'])['SurvWin4'].sum()/ survivalPla,    #after fourth winter
    df.groupby(['Pop'])['SurvSum4'].sum()/ survivalPla])    #after fourth summer
print(survivalNorway)

# turning the numpy array into a pandas dataframe with columns labels
df_survivalNorway = pd.DataFrame(data = survivalNorway, columns=['F1', 'F2', 'N', 'S'])

print(df_survivalNorway)

# creating the line plot

plt.plot(df_survivalNorway.index, df_survivalNorway)
plt.show()
