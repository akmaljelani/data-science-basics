# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 20:21:45 2021

@author: User-PC
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

df = pd.read_excel("C:/Users/User-PC/Desktop/Data Science/Data Science Assignment/1 EDA/Assignment_module02.xlsx")
df.head(10)
df.mean()
df.median()
df.mode()
df.var()
df.std()

df.describe()
plt.hist(df)

X = pd.read_excel("C:/Users/User-PC/Desktop/Data Science/Data Science Assignment/1 EDA/MeasureX.xlsx")
X.head()
X.mean()
X.var()
X.std()
plt.scatter(x=X['Name of company'], y=X['Measure X'], color='blue')


V = pd.read_excel("C:/Users/User-PC/Desktop/Data Science/Data Science Assignment/1 EDA/Venture.xlsx")
V.head()
V.std()
