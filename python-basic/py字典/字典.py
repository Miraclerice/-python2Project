# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/2/0002 21:25:37

'''
获取字典所有的值： dic.values()
获取字典所有的键： dic.keys()
获取字典所有的键值对： dic.items()
'''
dic = {"name": "admin", "age": 18, "height": 666}
values_ = (dic.values())
print values_

keys_ = (dic.keys())
print keys_

items_ = (dic.items())
print items_

dic["address"] = "shanghai"

print dic

print values_, keys_, items_
print values_[0]

dic.viewkeys()
dic.viewitems()
dic.viewvalues()

print dic.has_key("name")
print dic.has_key("name1")
