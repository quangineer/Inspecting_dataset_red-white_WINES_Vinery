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
df = pd.read_csv('winequality_edited.csv')
# print (df)

######Index does not support mutable operations. This command below is error
# df.columns[6]='change'


###Change the columns name:
New_list_of_columns = list(df.columns)
New_list_of_columns[6] = 'Inclusive Sulfur Dioxide'
df.columns = New_list_of_columns


###Another BUT SHORTER way to change columns name by using rename command:
red_data = red_data.rename(columns = {'total_sulfur-dioxide':'total_sulfur_dioxide'})

# print(df)

#histogram and scatterplot:
FA = df['fixed acidity']
a = FA.hist()

TSD = df['Inclusive Sulfur Dioxide']
b = TSD.hist()

PH = df['pH']
c = PH.hist()

AC = df['alcohol']
d = AC.hist()

e = df.plot.scatter(x='quality', y='volatile acidity')

f = df.plot.scatter(x='quality', y='residual sugar')

g = df.plot.scatter(x='quality', y='pH')

h = df.plot.scatter(x='quality', y='alcohol')

#GroupBy:
#group the data by color red and white to explore average quality factor each:
# print (df.groupby('color')['quality'].mean())

#group the data by color red and white and by quality to explore average pH factor each:
df.groupby(['quality', 'color'], as_index=False)['pH'].mean()

#This question is more tricky because unlike color, which has clear categories you can group 
#by (red and white) pH is a quantitative variable without clear categories. However, there is 
#a simple fix to this. You can create a categorical variable from a quantitative variable by 
#creating your own categories. pandas' cut function let's you "cut" data in groups. Using this, 
#create a new column called acidity_levels with these categories:

df.describe()['pH']
#result:
# count    6497.000000
# mean        3.218501
# std         0.160787
# min         2.720000
# 25%         3.110000
# 50%         3.210000
# 75%         3.320000
# max         4.010000
# Name: pH, dtype: float64

# Bin edges that will be used to "cut" the data into groups: Fill in the list below with five values you just found:
bin_edges = [2.72, 3.11, 3.21, 3.32, 4.01]

# Labels for the four acidity level groups: Name each acidity level category:
bin_names = ["High" ,"Moderately High" ,"Medium" ,"Low"]

#Create acidity levels column
df['acidity levels'] = pd.cut(df['pH'], bin_edges, labels=bin_names)

#Find the mean quality of each acidity level with groupby to know which acidity levels will give highest mean quality:
df.groupby('acidity levels')['quality'].mean()

df.to_csv('winequality_edited.csv', index=False)

###Note to self: How to select a columns in a dataframe:
#df.column_name or df['column_name'] # However, if you want to select more than one columns, 
#you only can use : df[["column_name", "column_name"]]

#Drawing conclusions using query:
# Re-read the csv file and work with general info of csv file first.
df.describe().alcohol
df.head()

#Finding the median for alcohol column to prepare for a split:
df.alcohol.median()

#Select samples with alcohol content less than the median and greater than the median: 

low_alcohol = df.query('alcohol <= 10.3')
high_alcohol = df.query('alcohol > 10.3')
# print (low_alcohol.quality.count())
# print (high_alcohol.quality.count())
# print (df.shape[0])

#Make sure no sample has Nal value in alcohol
# A = df.alcohol.notnull()
# print (A)

#Calculate mean of each low and high alcohol and answer the question of Do wines
# with higher alcoholic content receive better ratings?
# print (low_alcohol.quality.mean())
# print (high_alcohol.quality.mean())

#Get the median of residual_sugar:
(df['residual sugar'].median())

#select sample for residual sugar less and more than median:
# low_sugar = df.query('residual sugar <= 3.0')
# high_sugar = df.query('residual sugar > 3.0')
low_sugar = df[df['residual sugar'] <= 3.0]
high_sugar = df[df['residual sugar'] > 3.0]

# num_samples1 = df.shape[0]
# num_samples2 = low_sugar.quality.count() + high_sugar.quality.count()
# print (num_samples1)
# print (num_samples2)

#get mean quality rating for low and high sugar to answer DO sweeter wines receive better ratings?
print (low_sugar.quality.mean())
print (high_sugar.quality.mean())