import pandas as pd
import numpy as np
data=pd.read_csv('..//data/titanic.csv') #Load dataset by using read_csv
# data=pd.DataFrame('..//data/titanic.csv')
# print(data)
# print(data.shape)
# print(data.isnull)
# print(data.isna().any())
# print(data.isna().any().sum())
# print(data.describe)
# print(data.Survived)
# print(data.Survived)
# data.drop(['Cabin'],axis=1,inplace=True) #deleting cabin column
# print(data.isna().any())
# data.fillna(method='ffill',inplace=True)
# print(data.isna().any())
# data.fillna('0')
# print(data)
# data['Survived']=data['Survived'].map({1:'Yes',2:'No'})
# print(data)
# print(data['Survived'])
# print(data.groupby(['Sex','Survived'])['Survived'].count())

# print(pd.crosstab(index=data['Sex'],columns=data['Survived'].count()))
# print(pd.pivot_table(data,index=['Sex','Age'],aggfunc=np.sum))
# print(data.sort_values(by=['Pclass'])) #ascending order
print(data.sort_values(by=['Pclass','Age'],ascending=False)) #decending order
data['Survived']=data['Survived'].apply(lambda val:'Yes'if val==1 else 'No') #LAMBDA FUNCTION
print(data)