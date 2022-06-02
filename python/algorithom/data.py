#!/usr/bin/env python
# coding=utf-8

class Data(object):
    def __init__(self):
        self._data = []
        print "Data init"

    def add(self, x):
        self._data.append(x)

    def data(self):
        return iter(self._data)

d = Data()
d.add(1)
d.add(2)
d.add(3)

for x in d.data():
    print x

data = d.data()

while data.next():
    print "hello"
