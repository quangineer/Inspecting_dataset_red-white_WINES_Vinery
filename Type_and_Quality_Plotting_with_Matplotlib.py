import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

df = pd.read_csv('winequality_edited.csv')

ppp = df.rename(columns = {"Inclusive Sulfur Dioxide" : "inclusive sulfur dioxide"})

print (ppp.columns)