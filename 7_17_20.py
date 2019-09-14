#!/usr/bin/env python3
import re
"""
从右边起，每匹配3个数字就会有一个逗号，即：
1. 判断有没有逗号，如果没有逗号且小于等于3个数字，匹配
2. 如果没有逗号，但是大于4位数字，不匹配
3. 如果有逗号，判断逗号的右边是不是全为3位数字
"""

# 先匹配1-3个数字，然后再匹配零次或者多次 逗号加3个数字
mRegex = re.compile(r'^\d{1,3}(,\d{3})*$')
# mRegex = re.compile(r'\d{1,3}(,\d{3})*$')
def mFun(str):
	mo = mRegex.search(str)
	if mo == None:
		print("str = " + str + "	result = False")
	else:
		print("str = " + str + "	result = " + mo.group())
mFun('42')
mFun('1,234')
mFun('6,368,745')
mFun('12,34,567')
mFun('1234')


