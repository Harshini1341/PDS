# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nNF-jZGx391RBl-RD0QZlMCtDdWN1ClA
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pand
import scipy.stats as stat


encoded_data = pand.read_csv("/encoded_data.csv")


fr_w1 = encoded_data[encoded_data['Frailty'] == 1]['Weight']
fr_w2 = encoded_data[encoded_data['Frailty'] == 0]['Weight']


result = stat.ttest_ind(fr_w1, fr_w2)
t_stat = result.statistic
p_val = result.pvalue
print("Student's t test t_Statistic:", t_stat)
print("Student's t test p_value:", p_val)

alpha = 0.05

if p_val < alpha:
    print("Based on the statistical analysis, we have strong evidence to conclude that there is a significant difference in grip strength between the two groups.")
else:
    print("According to the statistical analysis, we do not have sufficient evidence to assert a significant difference in grip strength between the two groups.")