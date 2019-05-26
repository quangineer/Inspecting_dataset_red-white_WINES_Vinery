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
color_counts = wine_df.groupby(['color', 'quality']).count()