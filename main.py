import pandas as pd 
import numpy as np 
import matplotlib as plt

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

# print (red_data.head(10))

# print (white_data.head(10))

#Append dataframe:
wine_df = red_data.append(white_data)
# print (wine_df)

#make a new index for wine_df
wine_df = wine_df.reset_index()

#drop the old index for wine_df
wine_df = wine_df.drop(columns="index")
# print (wine_df)

wine_df.to_csv('winequality_edited.csv', index=False)
# print (wine_df.describe())



#check the border index between red and white dataset to see how they merge
# print (wine_df.iloc[1590:1609, :])



#Create a new dataframe for 'winequality_edited.csv'
NewDataFrame = pd.read_csv('winequality_edited.csv')
# print (NewDataFrame)

######Index does not support mutable operations. This command below is error
# NewDataFrame.columns[6]='change'


###Change the columns name:
New_list_of_columns = list(NewDataFrame.columns)
New_list_of_columns[6] = 'Inclusive Sulfur Dioxide'
NewDataFrame.columns = New_list_of_columns


###Another BUT SHORTER way to change columns name by using rename command:
red_data = red_data.rename(columns = {'total_sulfur-dioxide':'total_sulfur_dioxide'})

# print(NewDataFrame)

#histogram and scatterplot:
FA = df['fixed_acidity']
a = FA.hist()

TSD = df['total_sulfur_dioxide']
b = TSD.hist()

PH = df['pH']
c = PH.hist()

AC = df['alcohol']
d = AC.hist()

e = df.plot.scatter(x='quality', y='volatile_acidity')

f = df.plot.scatter(x='quality', y='residual_sugar')

g = df.plot.scatter(x='quality', y='pH')

h = df.plot.scatter(x='quality', y='alcohol')

