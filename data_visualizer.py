
# Visualizing survival of plants in an experiment in Norway to see if local plants survive better in their natural environment 
# than plants originating from a southern location.

# First install required packages

import matplotlib.pyplot as plt
import pandas as pd

# importing the data file
df = pd.read_csv('AlyrNorway_SpMaF12.txt', delim_whitespace = True)

# examine the column names
print(df.columns)

# For the plot, proportion of plants alive of each population (Sp and NC) need to be calculated separately at each time point:
# after planting outside, after the planting summer (0), after first, second, third and fourth winter and summer (1-4, respectively).


# Columns labeled as "Surv" show if each individual was alive or dead at the time they were surveyed.
# 'Win' shows the situation in the spring and shows after winter survival and 'Sum' refers to end of summer survey.  

# Survival is calculated as proportion of plants alive after planting at each time point, so that the effect of dying right after planting
# can be removed, as it is not natural and can be sourve of error.  

#survival_summer0 = df['SurvSum0'].sum()/df['SurvPla'].sum()


# proportion of plants alive at each time point in each popoultation relative to those alive after planting. This needs to be made into a dataframe.
survivalPla = df.groupby(['Pop'])['SurvPla'].sum()                      #number of plants alive after a few days after being planted outside
survivalSummer0 = df.groupby(['Pop'])['SurvSum0'].sum()/ survivalPla    #end of the summer they were planted
survivalWinter1 = df.groupby(['Pop'])['SurvSum0'].sum()/ survivalPla    #after first winter
survivalSummer1 = df.groupby(['Pop'])['SurvSum0'].sum()/ survivalPla    #after first summer
survivalWinter2 = df.groupby(['Pop'])['SurvSum0'].sum()/ survivalPla    #after second winter
survivalSummer2 = df.groupby(['Pop'])['SurvSum0'].sum()/ survivalPla    #after second summer
survivalWinter3 = df.groupby(['Pop'])['SurvSum0'].sum()/ survivalPla    #after third winter
survivalSummer3 = df.groupby(['Pop'])['SurvSum0'].sum()/ survivalPla    #after third summer
survivalWinter4 = df.groupby(['Pop'])['SurvSum0'].sum()/ survivalPla    #after fourth winter
survivalSummer4 = df.groupby(['Pop'])['SurvSum0'].sum()/ survivalPla    #after fourth summer



print(survivalPla)
print(survivalSummer0)


#print(survival_summer0)


#def draw_line_plot():
    # Draw line plot
    #fig,ax = plt.subplots()
    #plt.figure(figsize= (9,14))
    #plt.plot('value', c='b', data=df)
    #plt.ylabel('Survival')
    #plt.xlabel('Year')
    #plt.title('xxx')
    #plt.show()  
    

    # Save image and return fig (don't change this part)
    #fig.savefig('line_plot.png')
    #return fig
