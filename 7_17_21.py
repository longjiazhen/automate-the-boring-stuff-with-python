#!/usr/bin/env python3
import re
"""
匹配姓 Nakamoto 的完整姓名
假定名字 总是出现在姓前面，是一个大写字母开头的单词
"""
mRegex = re.compile(r'[A-Z]+[a-z]*\s[Nakamoto]$')
def mFun(str):
	mo = mRegex.search(str)
	if mo == None:
		print(str + ' False')
	else:
		print(str + ' True')
mFun('Satoshi Nakamoto')
mFun('Alice Nakamoto')
mFun('RoboCop Nakamoto')
mFun('satoshi Nakamoto') # 名字没有大写首字母
mFun('Mr. Nakamoto') # 前面的单词包含非字母字符
mFun('Nakamoto' ) # 没有名字
mFun('Satoshi nakamotos') # 姓没有首字母大写
