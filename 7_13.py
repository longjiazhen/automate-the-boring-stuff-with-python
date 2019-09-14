#!/usr/bin/env python3
import re
phoneRegex = re.compile(
	r'''( #用三重引号创建字符串
	(\d{3} | \(\d{3}\))? #可能有区号也可能没有，区号可能带括号也可能不带
	(\s | - | \.)? #可能有分隔符，分隔符是空格或者-或者.
	(\d{3}) #电话号码的前3个数字
	(\s | - | \.) #分隔符是空格或者-或者
	(\d{4}) #电话号码的后4个数字
	(\s*(ext|x|ext.)\s*\d{2,5})? #最后面还可能有ext或者x或者ext.或者2-5个数字
	)''', re.VERBOSE)
mo1 = phoneRegex.search('Call me at (123).456.7890 ext. 33333')
print(mo1.group())
mo2 = phoneRegex.search('aaa phone is (123).456.7890, email is info@nostarch.com. bbb phone is 333 415 863 9900, eamil is academic@nostarch.com. ccc phone is 222.415.863.9950, email is help@nostarch.com.')
print(mo2.group())
