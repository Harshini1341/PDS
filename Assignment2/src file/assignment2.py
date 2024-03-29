# -*- coding: utf-8 -*-
"""assignment2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1upXcA2z0iicmm4feZASDpJXKLXmkPFq1
"""

import pandas as pd
import numpy as np

df=pd.read_csv('/content/sample_data/train.csv')
df.head()

"""question 2

Remove the units from some of the attributes and only keep the numerical values (for
example remove kmpl from “Mileage”, CC from “Engine”, bhp from “Power”, and lakh from
“New_price”)
"""

data = pd.DataFrame(df)
# Remove units from specified columns
data['Mileage'] = df['Mileage'].str.extract('(\d+.\d+)').astype(float)
data['Engine'] = df['Engine'].str.extract('(\d+.\d+)').astype(float)
data['Power'] = df['Power'].str.extract('(\d+.\d+)').astype(float)
data['New_Price'] = df['New_Price'].str.extract('(\d+.\d+)').astype(float)


# Save the modified dataset to a CSV file
data.to_csv('/content/sample_data/modified_data.csv', index=False)
print(data.head())

"""question1

Look for the missing values in all the columns and either impute them (replace with mean,
median, or mode) or drop them. Justify your action for this task
"""

missing = df.isnull().sum()
print(missing)

mileage_median = data['Mileage'].median()
power_median = data['Power'].median()
# Impute missing values with the median
data['Mileage'].fillna(mileage_median, inplace=True)
data['Power'].fillna(mileage_median, inplace=True)

# Calculate the mode for "Engine" and "Seats" columns
engine_mode = data['Engine'].mode()[0]
seats_mode = data['Seats'].mode()[0]
# Fill missing values with the mode
data['Engine'].fillna(engine_mode, inplace=True)
data['Seats'].fillna(seats_mode, inplace=True)

data = data.drop("New_Price", axis=1)

# Save the modified DataFrame to a new CSV file
data.to_csv("/content/sample_data/modified_data1.csv", index=False)

# Check for missing values in each column
updated_missing_values = data.isnull().sum()
print(updated_missing_values)

"""question3

Change the categorical variables (“Fuel_Type” and “Transmission”) into numerical one hot
encoded value
"""

#Check the unique values of the Categorical columns : "Fuel_Type", Owner_Type and "Transmission"

print(data['Fuel_Type'].unique())
print(data['Transmission'].unique())
print(data['Owner_Type'].unique())
# Perform one-hot encoding for "Fuel_Type" and "Transmission" columns
data['Fuel_Type'].replace({'Diesel': 0, 'Petrol': 1, 'Electric': 2}, inplace=True)
data['Transmission'].replace({'Manual': 0, 'Automatic': 1}, inplace=True)
data['Owner_Type'].replace({'First': 1, 'Second': 2, 'Third': 3, 'Fourth & Above': 4}, inplace=True)

# Save the modified DataFrame to a new CSV file
data.to_csv("/content/sample_data/modified_data2.csv", index=False)

"""Question 4

Create one more feature and add this column to the dataset (you can use mutate function in
R for this). For example, you can calculate the current age of the car by subtracting “Year” value
from the current year
"""

import datetime
# Calculate the current year
currentyear = datetime.datetime.now().year

# Create the "Current_Age" feature by subtracting the "Year" from the current year
data['CurrentAge'] = currentyear - data['Year']

# Save the dataset with the new "CurrentAge" feature
data.to_csv("/content/sample_data/modified_data2.csv", index=False)