import pandas as pand

# Use pandas to read the CSV file into a DataFrame
dataFramework = pand.read_csv("/content/drive/MyDrive/FrailtyAnalysis/Frailty_Raw_Data.csv")

# Encode the "Frailty" column to 0 (No) and 1 (Yes)
dataFramework['Frailty'] = dataFramework['Frailty'].map({'N': 0, 'Y': 1})

# Print the modified DataFrame
print(dataFramework)

# Specify the file path for the output CSV file
modified_csv_file = '/content/drive/MyDrive/FrailtyAnalysis/cleaned_data.csv'

dataFramework.to_csv(modified_csv_file, index=True)