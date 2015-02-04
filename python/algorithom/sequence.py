#!/usr/bin/env python
# coding=utf-8

# range, 终点不包含在产生的序列中
# 生成序列0到9
range(10)

# 加步长的序列
# 生成的序列[0,3,6,9]
range(0, 10, 3)

# 序列号的索引
a = ['my', 'name', 'is', 'limin']

print "use range and len"
for i in range(len(a)):
    print i, a[i]

print "use enumerate"
for i, v in enumerate(a):
    print i, v
