import pandas as pds
import matplotlib.pyplot as mtlib
import seaborn as sb

# Load the dataset
df = pds.read_csv('/content/drive/MyDrive/StudentData/Clean_data.csv')

# Task 1: Visualization 1 - Heatmap visualization using seaborn
mtlib.figure(figsize=(10, 8))
sb.heatmap(data=df.corr(), annot=True, cmap='coolwarm', linewidths=.5)
mtlib.title('Correlation Heatmap')
mtlib.savefig('/content/drive/MyDrive/StudentData/correlation_heatmap.png')
mtlib.show()


# Task 2: Visualization 2- Pie Chart visualization 
avg_scr = df.groupby('gender')['reading score'].mean()
labels = avg_scr.index
sizes = avg_scr.values
mtlib.figure(figsize=(8, 6))
mtlib.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['#CD5C5C','#32CD32'])
mtlib.title('Average Reading Scores by Gender')
mtlib.savefig('/content/drive/MyDrive/StudentData/pie_chart.png')
mtlib.show()

# Task 3: Visualization 3 - Barplot of Parental Education Levels
mtlib.figure(figsize=(10, 6))
sb.countplot(data=df, x='parental level of education', hue='test preparation course')
mtlib.title('Barplot of Parental Education Levels by Test Preparation Course')
mtlib.xlabel('Parental Education Level')
mtlib.ylabel('Count')
mtlib.xticks(rotation=45, ha='right')
mtlib.savefig('/content/drive/MyDrive/StudentData/education_level_vs_test_prep.png')
mtlib.show()

# Task 4: Visualization 4 - Scatter Plot of Writing vs. Reading Scores
mtlib.figure(figsize=(8, 6))
sb.scatterplot(data=df, x='reading score', y='writing score', hue='gender')
mtlib.title('Scatter Plot of Writing vs. Reading Scores')
mtlib.xlabel('Reading Score')
mtlib.ylabel('Writing Score')
mtlib.savefig('/content/drive/MyDrive/StudentData/_reading_vs_writing.png')
mtlib.show()

# Task 5: Visualization 5 - Distribution of Lunch Types
mtlib.figure(figsize=(6, 4))
sb.countplot(data=df, x='lunch')
mtlib.title('Distribution of Lunch Types')
mtlib.xlabel('Lunch Type')
mtlib.ylabel('Count')
mtlib.savefig('/content/drive/MyDrive/StudentData/lunch_distribution.png')
mtlib.show()
