#!/usr/bin/env python3
import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('mo.group(1): ' + mo.group(1))
print('mo.group(2): ' + mo.group(2))
print('mo.group(0): ' + mo.group(0))
print('mo.group(): ' + mo.group())
print('mo.groups(): ', end = '')
print(mo.groups())
a, b = mo.groups()
print('a: ' + str(a))
print('b: ' + str(b))


