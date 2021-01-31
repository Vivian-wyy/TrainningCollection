# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 14:26:18 2021

@author: Wei Yuying
"""

# Action2: 统计全班的成绩

# 导入数据
import numpy as np
import pandas as pd
from pandas import Series
from pandas import DataFrame

data={'Chinese':[68,95,98,90,80],'Math':[65,76,86,88,90],'English':[30,98,88,77,90]}
df1 = DataFrame(data)
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'LiuBei', 'DianWei', 'XuChu'], columns=['Chinese', 'Math', 'English'])
# print(df1)
print(df2)


# 统计数据
# df3 = df2.describe()
df3 = df2.agg([np.mean, np.min, np.max, np.var, np.std])
print('1. 统计语文、英语、数学的平均成绩、最小成绩、最大成绩、方差、标准差: ')
print(df3)


df2.loc[:,'sum'] = df2.sum(axis=1)
# print(df2)
result = df2.sort_values('sum',ascending=False)
result.reset_index(inplace=True)
print('2. 对人进行总成绩排序: ')
print(result)


    