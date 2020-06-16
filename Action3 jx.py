# -*- coding: utf-8 -*-
"""
Action3: 对汽车质量数据进行统计
数据集：car_complain.csv
600条汽车质量投诉
Step1，数据加载
Step2，数据预处理
拆分problem类型 => 多个字段
Step3，数据统计
对数据进行探索：品牌投诉总数，车型投诉总数
哪个品牌的平均车型投诉最多

@author: JinXiang2
"""
import pandas as pd

result = pd.read_csv('D:\desktop\L1 jinxiang 11841\car_complain.csv')
result = result.drop('problem', 1).join(result.problem.str.get_dummies(','))
# print(result.columns)
tags = result.columns[7:]
#tag 表示所有投诉的问题
df= result.groupby(['brand'])['id'].agg(['count'])
df2= result.groupby(['brand'])[tags].agg(['sum'])
df2 = df.merge(df2, left_index=True, right_index=True, how='left')

df2.reset_index(inplace=True)
df2= df2.sort_values('count', ascending=False)
print(df2)

