import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

ppp = pd.read_csv('winequality_edited.csv')

df = ppp.rename(columns = {"Inclusive Sulfur Dioxide" : "inclusive sulfur dioxide"})

print (list(df.columns))