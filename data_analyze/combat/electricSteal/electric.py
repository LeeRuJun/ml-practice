#-*- coding:utf-8 -*-

import pandas as pd
from scipy.interpolate import lagrange

inputfile = "../../source/missing_data.xlsx"
outputfile = "../../source/missing_data_processed.xls"

data = pd.read_excel(inputfile, header=None, encoding="gb2312") # 读入数据

# 自定义列向量插值函数
def ployinterp_column(s, n, k=5):
    y = s[list(range(n-k, n)) + list(range(n+1, n+1+k))]
    y = y[y.notnull()] #剔除空值
    return lagrange(y.index, list(y))(n)

# 逐个元素判断是否需要插值
for i in  data.columns:
    for j in range(len(data)):
        if(data[i].isnull())[j]:
            data[i][j] = ployinterp_column(data[i], j)

data.to_excel(outputfile, header=None, index=False, encoding="gb2312") # 输出结果




