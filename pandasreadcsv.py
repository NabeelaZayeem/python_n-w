import pandas as pd
import numpy as np
data=pd.read_csv("..//data/tips.csv")
print(data.isna().any())
print(data.isna().sum())

print('--------------------------------')
tips_male_fm=data.filter(['tip','sex'])
print(tips_male_fm.groupby('sex').sum())
print('--------------------------------')
print(tips_male_fm.sex.value_counts())
print(tips_male_fm.sex.value_counts(normalize=True))
print('--------------------------------')
print(pd.crosstab(index=data['sex'],columns=data['smoker']))
# print(data)
print('--------------------------------')

day_wise=data.filter(['tip','day'])
print(day_wise.groupby('day').sum())
print('===============')
print(data.info)
print('===============')

print(data.columns)
print('===============')

print(data.describe)
print('===============')
print(data.head()) #first five rows
print('===============')

print(data.tail())#lAST FIVE RECORDS
