import pandas as pd
# talk: https://www.youtube.com/watch?v=qy0fDqoMJx8

values_df = pd.DataFrame({'AAA' : [4, 5, 6, 7], 'BBB' : [10, 20, 30, 40], 'CCC' : [100, 50, -30, -50]});
'''
   AAA  BBB  CCC
0    4   10  100
1    5   20   50
2    6   30  -30
3    7   40  -50
'''

len(values_df.index)
# 4

for i in range(0, len(values_df.index)): # range in python doesn't include the end parameter
   print(i)
'''
prints 
0
1
2
3
'''

# Create dict from df
values_dict = values_df.set_index('AAA')['BBB'].to_dict()
'''values_dict
Out: {4: 10, 5: 20, 6: 30, 7: 40}
values_dict[5]
Out: 20
'''

# Transform one column applying a function
values_df["BBB"] = values_df.transform({"BBB": lambda x: x**2})
'''
   AAA   BBB  CCC
0    4   100  100
1    5   400   50
2    6   900  -30
3    7  1600  -50
'''
# now transform all cells
values_df = values_df.transform(lambda x: x-2)
'''
   AAA   BBB  CCC
0    2    98   98
1    3   398   48
2    4   898  -32
3    5  1598  -52
'''
