#!/usr/bin/env python3
import re
#\d匹配1-9的数字，\s匹配空格制表符换行符，\w匹配任何字母数字或下划线字符，+表示匹配一次或者多次
mRegex = re.compile(r'\d+\s\w+')
print('findall():', end = '')
print(mRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))