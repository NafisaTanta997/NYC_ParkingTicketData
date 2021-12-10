"""
Name: Nafisa Tanta
Email: Nafisa.Tanta67@myhunter.cuny.edu
Resources:
"""
# libraries
import numpy as np
import pandas as pd
from numpy import mean
import math

# Data
readfile=pd.read_csv('Rent2019.csv')
df = pd.DataFrame(readfile)

# STUDIO
dfStudio = df.copy()
dfStudio = dfStudio.dropna(how='any',axis=0)
dfStudio = dfStudio.pop("Studio")

studio = []
for i in dfStudio:
    i = i.replace(',', '')
    studio.append(float(i))

mean = sum(studio)/len(studio)
print("Average rent of Studio Apartments in NYC is: ", mean)

# 1 BEDROOM
df1BR = df.copy()
df1BR = df1BR.dropna(how='any',axis=0)
df1BR = df1BR.pop("1 Bedroom")

oneBR = []
for i in df1BR:
    i = i.replace(',', '')
    oneBR.append(float(i))

mean = sum(oneBR)/len(oneBR)
print("Average rent of 1 Bedroom Apartments in NYC is: ", mean)

# 2 BEDROOM
df2BR = df.copy()
df2BR = df2BR.dropna(how='any',axis=0)
df2BR = df2BR.pop("2 Bedroom")

twoBR = []
for i in df2BR:
    i = i.replace(',', '')
    twoBR.append(float(i))

mean = sum(twoBR)/len(twoBR)
print("Average rent of 2 Bedroom Apartments in NYC is: ", mean)

