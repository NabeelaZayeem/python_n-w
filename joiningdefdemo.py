import pandas as pd

d1={'Name':['pankaj','Meghna','Lisa'],'country':['India','India','India']}
df1=pd.DataFrame(d1)
print(df1)
df2=pd.DataFrame({'ID':[1,2,3],'Name':['pankaj','Anupam','Amit']})
print(df2)
df_merged=df1.merge(df2,how='right',on=df2['ID'])
print(df_merged)