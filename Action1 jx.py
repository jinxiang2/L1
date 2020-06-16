# -*- coding: utf-8 -*-
"""
Action1：求2+4+6+8+...+100的求和，用Python该如何写

@author: JinXiang2
"""
import numpy as np

x1 = np.arange(2,101,2)

sum = 0
for number in x1:
    sum = sum + number
print(sum)


