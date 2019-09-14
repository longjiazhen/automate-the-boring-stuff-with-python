#!/usr/bin/env python3
import re
phoneRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneRegex.search('Cell: 415-555-1234 Work: 123-456-7890')
print('mo.group(): ' + mo.group())

print('findall1: ', end = '')
print(phoneRegex.findall('Cell: 415-555-1234 Work: 123-456-7890'))

phoneRegex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
print('findall2: ', end = '')
print(phoneRegex.findall('Cell: 415-555-1234 Work: 123-456-7890'))


