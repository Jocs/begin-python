#!/usr/bin/env python
# -*- coding:utf8 -*-

fourth = raw_input('Year: ')[3]
print fourth

#分片
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
partial = number[2:-2]
print partial
print number[-3:]
#复制序列
anotherNumber = number[:]
print anotherNumber
#步长
print number[::2]

#序列相加
number2 = [1, 2, 3] + [4, 5, 6]

#序列的乘法
str1 = 'python ' * 4
print str1
print [10] * 10
print [None] * 10