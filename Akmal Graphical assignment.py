# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 21:26:41 2021

@author: User-PC
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/User-PC/Desktop/Data Science/Data Science Assignment/2 Graphical Representation/Q1_a.csv')
df.head()
df.mean()
df.mode()
df.median()
df.skew()
df.kurt()

df.speed.skew()

cd = pd.read_csv('C:/Users/User-PC/Desktop/Data Science/Data Science Assignment/2 Graphical Representation/Q2_b.csv')
cd.head()
cd.mean()
cd.mode()
cd.median()
cd.skew()
cd.kurt()


mean = 200
sd = 30

import statistics
dt = [34,36,36,38,38,39,39,40,40,41,41,41,41,42,42,45,49,56]
average = statistics.mean(dt)
print (average)

var = statistics.variance(dt)
print(var)

std = statistics.stdev(dt)
print(std)
