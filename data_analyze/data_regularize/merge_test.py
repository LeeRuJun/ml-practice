import  pandas as pd

df1 = pd.DataFrame({'key':['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df2 = pd.DataFrame({'key':['a', 'b', 'd'], 'data2': range(3)})

#print(pd.merge(df1, df2,on='key')) # 显示指明链接列

df3 = pd.DataFrame({'lkey':['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df4 = pd.DataFrame({'rkey':['a', 'b', 'd'], 'data2': range(3)})

#print(pd.merge(df3, df4,left_on= 'lkey', right_on = 'rkey' ))

#print(pd.merge(df1, df2, how='right')) #// left ,right ,outer


left = pd.DataFrame({'key1':['foo', 'foo', 'bar'],
                    'key2':['one', 'two', 'one'],
                    'lval':[1, 2, 3]})

right = pd.DataFrame({'key1':['foo', 'foo', 'bar', 'bar'],
                      'key2':['one','one', 'one', 'two'],
                      'rval':[4, 5, 6, 7]})

#print(pd.merge(left, right, on = ['key1', 'key2'], how='outer'))
