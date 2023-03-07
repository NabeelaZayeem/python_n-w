import pandas as pd
d={'Team':["India","Pakistan","UK","USA","UAE"],
   'Rank':[1,2,3,4,5],
   'winningper':['50','60','40','80','70']
   }
df=pd.DataFrame(d)
print(df)

###############################
print('--------------------------')

df1=df.rename(columns={'Rank': 'Ranking'})
print(df1)
############
# inorder to make changes in the original dataset permanantly use    'inplace'
print('--------------------------')
df=pd.DataFrame(d)
df.rename(columns={'Rank': 'Ranking'},inplace=True)

# iloc----index based
print(df.iloc[:,[0,1]    ])
print("printing 3 rows from second third column ")
print(df.iloc[:3,2])
print('--------------------------')

# Using loc-label selected
df=pd.DataFrame(d)
df.rename(columns={'Rank': 'Ranking'},inplace=True)
df.set_axis(df['Team'],inplace=True)
print(df.loc[df['Ranking']>=3])
print(df)
print('--------------------------')

#deleting records permanantly
# df.drop([3,4],axis=0,inplace=True)
# print(df)
# df.drop(['winper'],axis=1,inplace=True)

# print(df)
print(df.isna().any())
print(df.isna().sum())