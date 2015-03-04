#!/usr/bin/env python
# coding=utf-8

class User(object):
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self):
        del self.__name

u = User()
u.name = "limin"
print u.__dict__
