#!/usr/bin/env python3

"""
第一个词是 Alice、Bob 或 Carol，第二个词是 eats、pets 或 throws，
第三个词是 apples、cats 或 baseballs。该句 子以句点结束。这个正则表达式应该不区分大小写
"""

import re
mRegex = re.compile(r'^(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)',
	re.IGNORECASE)
def mFun(str):
	mo = mRegex.search(str)
	if mo == None:
		print(str + " False")
	else:
		print(str + " True")

mFun('Alice eats apples.')
mFun('Bob pets cats.')
mFun('Carol throws baseballs.')
mFun('Alice throws Apples.')
mFun('BOB EATS CATS')
mFun('RoboCop eats apples.')
mFun('ALICE THROWS FOOTBALLS.')
mFun('Carol eats 7 cats.')