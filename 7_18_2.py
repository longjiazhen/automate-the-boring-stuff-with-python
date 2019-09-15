#!/usr/bin/env python3

"""
strip()的正则表达式版本
写一个函数，它接受一个字符串，做的事情和 strip()字符串方法一样。
如果只传入了要去除的字符串，没有其他参数，那么就从该字符串首尾去除空白字符。
否则，函数第二个参数指定的字符将从该字符串中去除。
"""

import re


def mFun(mstr, sep = "\s"):
	# mRegex = re.compile(r'(^[%s]* | [%s]*$)' % (sep, sep))
	mRegex1 = re.compile(r'(^[%s]*)' % sep)
	mRegex2 = re.compile(r'([%s]*$)' % sep)
	mo1 = mRegex1.search(mstr)
	mo2 = mRegex2.search(mstr)
	if mo1 != None:
		mstr = mRegex1.sub("", mstr)
	if mo2 != None:
		mstr = mRegex2.sub("", mstr)
	return mstr

mstr = "qkq   AqAqqA qqkqq"
print("Before:")
print(mstr)
print("After:")
print(mFun(mstr, "q"))

