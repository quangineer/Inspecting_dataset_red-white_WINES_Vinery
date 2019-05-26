import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
% matplotlib inline
import seabron as sns
sns.set_style('darkgrid')


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
