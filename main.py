import pandas as pd 

red_data = pd.read_csv('winequality-red.csv', sep=';')
white_data = pd.read_csv('winequality-white.csv', sep=';')

# print((red_data).info())
print((red_data).describe())
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