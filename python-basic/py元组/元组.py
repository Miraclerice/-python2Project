# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/2/0002 19:55:46
# 比较

t = ('aa', 'bb', 'cc', "dd", "ee")
t1 = ('aa', 'bb', 'cc', "dd", "ee", "ff")
'''
cmp(val1,val2)
内建函数
如果比较字符串，列表等集合,从左往右逐个比较
val1 > val2  1
val1 = val2  0
val1 < val2  -1
python3.x不支持

python3使用比较运算符比较
'''
print cmp(t, t1)
print cmp(t1, t1)
print cmp(t1, t)