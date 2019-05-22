import pandas as pd 

red_data = pd.read_csv('winequality-red.csv', sep=';')
white_data = pd.read_csv('winequality-white.csv', sep=';')

print((red_data).info())