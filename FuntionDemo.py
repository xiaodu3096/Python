#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 21/12/2017 22:47
# @Author  : DaBai
# @Site    : 
# @File    : FuntionDemo.py
# @Software: PyCharm

# print(abs(-12.1))#返回数据的绝对值
# fun = len
# print(fun('1231231232'))
#
# def hello(): #自定义函数
#     print('Hello xiaodu')
# hello() #调用函数

# def paramone(str):
#     print('this para is:',str)
#     print('我是传过来的参数，我的值是：',str)
# paramone('Hello',' world')
# def personInfo(age,name):
#     print('年龄：',age)
#     print('名称：',name)
#     return
#
# print('---------按参数顺序传入参数----------')
# personInfo(21,'小杜')
# print('---------不按参数顺序传入参数，指定参数名----------')
# personInfo(name='xiaomeng',age=21)
# print('---------按参数顺序传入参数，并指定参数名--------')
# personInfo(age=23,name='xiaoqiang' )
# def defaultparam(name,age=23):
#     print('Hi,My name is： ',name)
#     print('My age is： ',age)
#     return
#
# defaultparam('小杜',25)
# def defaltParma(name,age=21):
#     print('Hi My name is ：',name)
#     print('我今年：',age)
#     return
# other = {'城市':'北京','爱好':'编程'}
# def personInfo(name,number,**kw):
#     print('姓名:',name,'学号:',number,'其他:',kw)
#     return
#
# personInfo('小杜','1002',城市=other['城市'],爱好=other['爱好'])
# personInfo('小杜','1002',**other)

# x = 50
# def func(x):
#     print('x等于',x)
#     x = 2
#     print('x等于',x)
# func(x)
# print('x等于',x)

# total = 0
# def sum(arg1,arg2):
#     total = arg1 + arg2
#     print('函数内的局部变量:',total)
#     return total
# def totalPrint():
#     print('total的值是:',total)
#     return total
# print('函数求和结果为:',sum(10,20))
# totalPrint()
# print('函数外事全局变量:',total)
#
#
# num = 100
# def func():
#     num = 200
#     print('函数体重num的值是',num)
#     pass
# func()
# print('函数体外num的值是',num)

# num = 100
# print('函数前调用num的值为:',num)
# def func():
#     global num
#     num  = 200
#     print('函数体中num的值为:',num)
# func()
# print('函数调用结束后num的值为:',num)

# def clac_sum(*arg):
#     ax = 0
#     for n in arg:
#         ax += n
#     return ax
#     # return clac_sum()


# def sum_late(*args):
#     def clac_sum():
#         ax = 0
#         for n in args:
#             ax += n
#         return ax
#     return clac_sum
# print('调用sum_late的结果是',sum_late(1,2,3,4))
# clac_sum = sum_late(1,2,3,4)
# print('调用clac_num的结果是',clac_sum())
#
# f1 = sum_late(1,2,3)
# f2 = sum_late(1,2,4)
# print(f1)
# print(f2)
# print('f1 == f2的结果是',f1 == f2)
# def count():
#     fs = []
#     for i in range(1,4):
#         def f():
#             return i * i
#         print(fs)
#         fs.append(f)
#     return fs
#
# f1,f2,f3 = count()
#
# print('f1的结果是',f1())
# print('f2的结果是',f2())
# print('f3的结果是',f3())
#
# def counts():
#     def f(j):
#         def g():
#             return j * j
#         return g
#     fs = []
#     for i in range(1,4):
#         fs.append(f(i))#f(i)立刻被执行，因此I的当前值被传入f()
#     return fs
#
# f1,f2,f3 = counts()
# print('f1的结果是',f1())
# print('f2的结果是',f2())
# print('f3的结果是',f3())
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
# print('调用递归函数执行结果为:',fact(10))
#
#
# def facts(n):
#     return fact_iter(n,1)
#
# def fact_iter(num,pro):
#     if num == 1:
#         return  pro
#     return fact_iter(num - 1,num * pro)
#
# print('调用递归函数执行结果为:',fact(1000))
#
# L1 = [1,2,3,4,5,6]
# L2 = []
# for i in L1:
#     if i > 3:
#         L2.append(i)
#
# print('数组中大于3的数据有:',L2)
#
# print('数组中大于3的数据有:',[item for item in filter(lambda x:x>3,L1)])
#
# t = lambda : False
# print(t())

from functools import partial

def mod(n , m):
    return n % m


mod_by_101 = partial(mod,101)

print('自定义函数，100对7取余结果为:',mod(100,7))
print('调用偏函数，100对7取余结果为:',mod_by_101(7))






