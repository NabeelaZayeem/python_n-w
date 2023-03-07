import pandas as pd
d={'Team':["India","Pakistan","UK","USA","UAE"],
   'Rank':[1,2,3,4,5]
   }
Team=["India","Pakistan","UK","USA","UAE"]
s=pd.Series(Team)
print(s)
print('-----------------------')
s=pd.Series(Team,index=['a','b','c','d','e'])
print(s)
