#!/usr/bin/env python
# coding=utf-8

def revert(L):
    if len(L) == 1:
        print L[0]
    else:
        revert(L[1:])
        print L[0]

revert('abcdefg')
