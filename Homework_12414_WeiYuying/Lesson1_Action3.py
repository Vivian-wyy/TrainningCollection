# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 14:59:05 2021

@author: Wei Yuying
"""

# Action3: 对汽车质量数据进行统计

import pandas as pd

# 数据加载
df = pd.read_csv('./car_complain.csv')

# 数据清洗
def f(x):
    x = x.replace('一汽-大众', '一汽大众')
    return x
df['brand'] = df['brand'].apply(f)

# 数据预处理，拆分problem类型 => 多个字段
df1 = df.drop('problem', axis=1).join(df.problem.str.get_dummies(','))
# print(df)

# 1. 数据统计 - 品牌投诉总数
result1 = df1.groupby(['brand'])['id'].agg(['count'])
print(result1)

# 2. 数据统计 - 车型投诉总数
result2 = df1.groupby(['brand','car_model'])['id'].agg(['count'])
print(result2)

# 3. 数据统计 - 哪个品牌的平均车型投诉最多
# 拆分车型，统计每个品牌下面车型数量
df2 = df.drop_duplicates('car_model').join(df.car_model.str.get_dummies())
tags = df2.columns[7:]
result3 = df2.groupby(['brand'])['car_model'].agg(['count'])

# 先合并，再计算平均值
result3 = result1.merge(result3, left_index=True, right_index=True, how='left')
result3 = result3.rename(columns={'count_x': 'complains','count_y':'car_models'})
result3.loc[:,'mean_complains'] = result3['complains']/result3['car_models']
result = result3.sort_values('mean_complains',ascending=False)
print(result)
result.to_excel('./result.xlsx')