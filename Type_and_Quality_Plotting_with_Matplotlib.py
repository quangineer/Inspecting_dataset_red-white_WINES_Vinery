import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
# % matplotlib inline
# import seabron as sns
# sns.set_style('darkgrid')


df = pd.read_csv('winequality_edited.csv')

wine_df = df.rename(columns = {"Inclusive Sulfur Dioxide" : "inclusive sulfur dioxide"})


# Create arrays for red bar heights and white bar heights:
# Remember, there is a bar for each combination of color and quality rating. Each bar's height is
# based on the proportion of samples (counts) of that color with (a given/certain) that quality rating.
# 1. RED BAR PROPORTIONS = COUNTS FOR EACH QUALITY RATING/TOTAL # OF RED SAMPLES
# 2. WHITE BAR PROPORTIONS = COUNTS FOR EACH QUALITY RATING/TOTAL # OF WHITE SAMPLES

# GET COUNTS/NUMBERS OF EACH RATING AND COLOR:
color_counts = wine_df.groupby(['color', 'quality']).count()['pH']
# WHY ['pH']: because of the count, so all the values for all columns are the same, so we just pick a random/arbitrary column.
color_totals = wine_df.groupby('color').count()['pH']

# get RED proportions by dividing red rating counts by total # of red samples:
red_proportions = color_counts['red']/color_totals['red']

# get WHITE proportions by dividing white rating counts by total # of white samples:
white_proportions = color_counts['white']/color_totals['white']

# NOW to plot proportions on a bar chart
# Set the x coordinate location for each rating group and width of each bar:
ind = np.arange(len(red_proportions))   # The x locations for the groups
# Why we take length of red_proportions instead of length of white_proportions? 
# To show that there is a mismatch: objects (of white color wines) cannot be broadcast to a single shape
# Why?
# because red_proportions has the length of 6, meanwhile white_proportions has the length of 7, thus it
# does not match compatibly. 
# SOLUTIONS:
# YOU CAN EITHER change the ind to "ind = np.arange(len(white_proportions))" to get the longer value as 
# the # of locations since it can cover for the shorter value of red counts. 
# OR YOU CAN COME BACK to red_proportions and add 1 more value as such "red_proportions['9'] = 0" because
# there is no quality rating of 9 for red_proportions. Creating one will help match everything.

width = 0.35 # the width of the bars



