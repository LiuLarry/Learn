#!/usr/bin/env python
# coding=utf-8

# 判断一个字符串中的字符是否唯一

def isUnique(str):
    ch = [False] * 26

    for s in str:
        index = ord(s) - ord('a')

        if ch[index]:
            return False
        else:
            ch[index] = True
    return True

print isUnique("abced")
print isUnique("aa")
