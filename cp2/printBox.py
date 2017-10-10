#!/usr/bin/env python
# -*- coding:utf8 -*-

sentence = raw_input('Whatever you input: ')
screenWidth = 80
textWidth = len(sentence)
boxWidth = textWidth + 6
paddingWidth = (screenWidth - boxWidth) // 2

print '-' * screenWidth
print ' ' * paddingWidth + '|' + ' ' * boxWidth + '|'
print ' ' * paddingWidth + '|   ' + sentence + '   |' 
print ' ' * paddingWidth + '|' + ' ' * boxWidth + '|'
print '-' * screenWidth