#!/usr/bin/env python
# coding=utf-8

'''
欧拉回路算法

1. 定义
若图G中存在这样的路径，使得通过G中的每条边一次，称该路径为欧拉路径，
若该路径是一个环，称为欧拉回路。

2. 判断条件
# 一个无向图存在欧拉回路，当且仅当图中所有顶点的度数为偶数，且为连通图。
# 一个有向图存在欧拉回路，当且仅当图中所有顶点的入度等于出度，且为连通图。
'''
