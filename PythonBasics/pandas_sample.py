import pandas as pd

df = pd.DataFrame(
   {'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]});
'''
   AAA  BBB  CCC
0    4   10  100
1    5   20   50
2    6   30  -30
3    7   40  -50
'''

len(df.index)
# 4

for i in range(0,len(df.index)): # range in python doesn't include the end parameter
   print i
'''
prints 
0
1
2
3
'''
