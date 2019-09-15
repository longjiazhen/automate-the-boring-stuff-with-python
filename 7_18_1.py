#!/usr/bin/env python3

"""
写一个函数，它使用正则表达式，确保传入的口令字符串是强口令。强口令的定义是:
长度不少于 8 个字符，同时包含大写和小写字符，至少有一位数字。
你可能需要用多个正则表达式来测试该字符串，以保证它的强度。
"""

import re

# 长度不少于8个字符
Regex1 = re.compile(r'.')
# 同时包含大写和小写字母
Regex2 = re.compile(r'[A-Z]')
Regex3 = re.compile(r'[a-z]')
# 至少有一位数字
Regex4 = re.compile(r'[0-9]')

def mFun(mstr):
	if len(Regex1.findall(mstr)) < 8:
		print("Regex1 False")
		return False
	mo2 = Regex2.search(mstr)
	if mo2 == None:
		print("Regex2 False")
		return False
	mo3 = Regex3.search(mstr)
	if mo3 == None:
		print("Regex3 False")
		return False
	mo4 = Regex4.search(mstr)
	if mo4 == None:
		print("Regex4 False")
		return False
	return True

mstr = "kkkkkk2AAAaAAA"
print(mstr + " " + str(mFun(mstr)))
