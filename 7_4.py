#!/usr/bin/env python3
import re

greedyRegex = re.compile(r'(ha){3,5}')
mo1 = greedyRegex.search('hahahahaha')
print('mo1.group(): ' + mo1.group())

nongreedyRegex = re.compile(r'(ha){3,5}?')
mo2 = nongreedyRegex.search('hahahahaha')
print('mo2.group(): ' + mo2.group())

"""
1. import re
2. re.compile(r'正则表达式')
3. search('待匹配字符串')
4. group()
"""