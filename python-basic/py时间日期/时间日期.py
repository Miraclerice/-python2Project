# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/3/0003 10:12:49

# 获取当前cpu时间
# python3.8后不支持time.clock()
import time

startClock = time.clock()
for i in range(0, 1000):
    print(i)


endClock = time.clock()

print(endClock-startClock)