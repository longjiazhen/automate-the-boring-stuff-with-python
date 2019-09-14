#!/usr/bin/env python3
import re
"""
从右边起，每匹配3个数字就会有一个逗号，即：
1. 判断有没有逗号，如果没有逗号且小于等于3个数字，匹配
2. 如果没有逗号，但是大于4位数字，不匹配
3. 如果有逗号，判断逗号的右边是不是全为3位数字
"""

"""
mRegex = re.compile(r'\d{1,3}(,\d{3})*$')
def mFun(str):
	mo = mRegex.search(str)
	if mo == None:
		print("mo == None")
	else:
		print("mo.group() = " + mo.group())
mFun('42')
mFun('1,234')
mFun('6,368,745')
mFun('12,34,567')
mFun('1234')
"""

#mRegex = re.compile(r'[A-Z]+[a-z]*[Nakamoto]$')
Regex = re.compile(r'[A-Z]+')
def mFun(str):
	mo = mRegex.search(str)
	if mo == None:
		print(str + ' False')
	else:
		print(str + ' True')
mFun('Satoshi Nakamoto')
mFun('Alice Nakamoto')
mFun('RoboCop Nakamoto')
mFun('satoshi Nakamoto')
mFun('Mr. Nakamoto')
mFun('Nakamoto' )
mFun('Satoshi nakamotos')
