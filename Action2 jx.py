# -*- coding: utf-8 -*-
"""
班里有5名同学，现在需要你用Python来统计下这些人在语文、英语、数学中的平均成绩、
最小成绩、最大成绩、方差、标准差。然后把这些人的总成绩排序，得出名次进行成绩输出
（可以用numpy或pandas）

@author: JinXiang2
"""
from pandas import Series, DataFrame
data = {'语文': [68, 95, 98, 90,80], '数学': [65, 76, 86, 88, 90], '英语': [30, 98, 88, 77, 90]}
df1 = DataFrame(data)
df2 = DataFrame(data, index=['张飞', '关羽', '刘备', '典韦', '许褚'], columns=['语文', '数学', '英语'])
print(df2)
print(df2.describe())
print(df2.var())
zongfen=df2.sum(1)
zongfen2= zongfen.sort_values(0, ascending=False)
print(zongfen2)