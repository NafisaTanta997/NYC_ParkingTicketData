"""
Name: Nafisa Tanta
Email: Nafisa.Tanta67@myhunter.cuny.edu
Resources:
"""

# Title: NYC Parking Ticket Data
# File : ParkingViolationsIssued2020.csv

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
A function that filters all the columns in the
DataFrame and return a DataFrame with only the
relevant columns
"""
def dataFrameFilter(df):
    
    df_copy = df.copy()

    df.dropna(axis=1, how='any', inplace=True)
    print(df.columns.values)
    df.drop(df.columns[[0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16]], axis=1, inplace=True)
    df['Vehicle Type'] = df_copy['Vehicle Body Type']
    df['Vehicle Make'] = df_copy['Vehicle Make']

    return df

# Takes input file name
inputfile = input("Enter input file name: ")

# Takes output file name
file_output = "file_output"

# Reads input file
readfile = pd.read_csv(inputfile)

# Locates the "Registration State" column
# Locates all the rows in this column where the state is not "99"
read = readfile.loc[readfile["Registration State"] != '99']

# List of unique states in read
states = read['Registration State'].unique().tolist()
states.sort()
states.pop()

# Group states by total violations
dfStates = pd.DataFrame(read)
dfStates = dfStates.groupby('Registration State')['Registration State'].count()

print(dfStates)

# Creates the comparison figure
fig = dfStates.plot(figsize = (12,8))

# Titles and Grid
plt.title("Violations Issued By State, 2020", loc='left', pad = 29, fontsize = 20, weight = 'bold')
fig.text(x=-2.75, y=900000, s="CSci 39542, Hunter College | Source: OpenData NYC", fontsize = 14)
plt.grid()

# Axes edit
plt.ylim([0, 1500000])

# Hide the right and top spines

fig.spines['right'].set_visible(False)
fig.spines['top'].set_visible(False)
fig.spines['left'].set_visible(False)
fig.tick_params(left = False)
fig.tick_params(bottom = False)

# Save to output file
plt.savefig(file_output)

plt.show()






