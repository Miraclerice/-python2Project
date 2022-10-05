# -*- coding: UTF-8 -*-
# @author  : M_Xie
# @date    : 2022/10/5/0005 9:30:54

# class Person(object):
#     pass
#
#
# print(Person.__bases__)

# python2.x环境下测试
# property在经典类使用方式一
class Person:
    def __init__(self):
        self.__age = 18

    def set_age(self, age):
        print "setAge..."
        self.__age = age

    def get_age(self):
        print "getAge..."
        return self.__age

    # 参数顺序不能反
    age = property(get_age, set_age)


# p = Person()
# # 经典类不能修改属性，只会新增属性，只关联了property的读取方法
# p.age = 666
# print p.age
# print p.__dict__


# property在经典类使用方式二
class Animal:
    def __init__(self):
        self.__age = 15

    @property
    def age(self):
        print "get___________"
        return self.__age

    @age.setter
    def age(self, age):
        print "set__________"
        self.__age = age

animal = Animal()
# # 经典类不能修改属性，只会新增属性，只关联了property的读取方法
animal.age = 666
print animal.age
print animal.__dict__
