#!/usr/bin/env python
# coding=utf-8

def powerset(p):
    '''子集
    '''
    aa =[[]]
    for i in p:
        l = len(aa)
        for j in aa[:l]:
            k = [i]
            k = j + k
            aa.append(k)

    print aa

powerset([1,2])

powerset([1,2,3,4,5,6,7])
