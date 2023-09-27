
import pandas as pd
 
# reading the CSV file and storing it to dataframe 'raw_data'
raw_data = pd.read_csv('/content/drive/MyDrive/StudentData/StudentsPerformance.csv')

#cleaning data -> In this case data is clean. So, writing dataframe to data-clean folder
raw_data.to_csv('/content/drive/MyDrive/StudentData/Clean-data.csv',index=False)

#displaying dataframe
raw_data
