标准库概览
=======================

操作系统接口
-----------------------
os 模块提供了很多与操作系统相关联的函数
    >>> import os
    >>> os.getcwd()
    >>> os.system('mkdir test')

上例中应该用 *import os* 风格而非 *from os import **。这样可以保证随操作系统不同而有所变化的 *os.open()* 不会覆盖内置函数 *open()*


