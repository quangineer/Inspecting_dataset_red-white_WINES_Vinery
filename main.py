import pandas as pd 
import numpy as np 

red_data = pd.read_csv('winequality-red.csv', sep=';')
white_data = pd.read_csv('winequality-white.csv', sep=';')

# print((red_data).info())
# print((red_data).describe())
# print ((red_data).tail(5))
# print ((red_data).head(5))

# print((white_data).info())
# print((white_data).describe())
# print ((white_data).tail(5))
# print ((white_data).head(5))

# print (red_data.isnull().sum())
# print (white_data.isnull().sum())

# print (white_data.duplicated().sum())
# print (white_data[white_data.duplicated()])

# print (red_data.nunique())
# print (white_data.nunique())

#give number of row count
# print (red_data.shape[0])
# print (white_data.shape[0])

#give number of column count
# print (red_data.shape[1])
# print (white_data.shape[1])

#Create color array for red dataframe:
color_red = np.repeat('red', red_data.shape[0])
color_white = np.repeat('white', white_data.shape[0])

#Add arrays to the red and white dataframe respectively:
red_data['color'] = color_red
white_data['color'] = color_white 

print (red_data.head(10))

print (white_data.head(10))