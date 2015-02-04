#!/usr/bin/env python
# coding=utf-8

#=====================================================================
# case 1
i = 5
# 默认值在函数定义作用域被解析
def f1(arg=i):
    print arg

i = 6
# 输出 5
f1()

#====================================================================
# case 2
'''
case 1中的参数默认值在定义的时候被解析，默认值只被解析一次，这造成字
典，列表或大部分实例等可变对象的行为会与期望的值不一致。
'''
def f2(a, L=[]):
    L.append(a)
    return L
'''
output:
[1]
[1, 2]
[1, 2, 3]
'''
print f2(1)
print f2(2)
print f2(3)

#====================================================================
# case 3
'''
解决 case 2中的问题可以这样
'''
def f3(a, L=None):
    if L is None:
        L = []
    L.append(a)
    
    return L


#====================================================================
# case 4
# 关键字参数
def f4(vol, state='state', type='type'):
    print "vol=%s, state=%s, type=%s" % (vol, state, type)

f4('vol')
f4('vol', 'new state')

#===================================================================
# case 5
'''
函数参数为**name时，可接收一个字典，参数形如*name时，接收一个元组
'''
def f5(kind, *args, **keywords):
    print "kind", kind
    print "args:", args
    for k, v in keywords.items():
        print "key=%s, value=%s" % (k, v)

f5('dog', '1', '2', key1='a', key2='b')
