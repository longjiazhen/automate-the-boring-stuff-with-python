#!/usr/bin/env python3
import re, pyperclip
"""
#1、用ctrl-A选择所有文本，ctrl-C复制 -- pyperclip.paste()
#2、运行程序，找出所有电话号码和邮箱地址 -- 2个正则表达式，一个匹配电话号码，一个匹配邮箱地址，
#找到所有匹配，放入到字符串中，如果没有匹配中的话，显示某种信息
#3、将这些电话号码和邮箱地址粘贴到剪切板 -- pyperclip.copy()
"""
temp = str(pyperclip.paste())
#print(temp)
phoneRegex = re.compile(
	r'''
	(\d{3}|\(\d{3}\))?
	(-|.|\s)?#可能有区号，也可能没有，区号可能有括号，也可能没有
	#可能有分隔符，分隔符是-或者.或者空格,re.VERBOSE会忽略空格，真正想要匹配空格的话得用\s
	(\d{3}) #接下来是3个数字
	(-|.|\s) #分隔符
	(\d{4}) #接下来是4个数字
	(\s*(ext|x|ext.)\s*\d{2,5})? #可能有扩展部分：0-几个空格然后ext或者x或者ext.再接着0-几个空格然后是2-5个数字
	''', re.VERBOSE)
mailRegex = re.compile(r'\w+[@]\w+[.]\w+')
matches = []
for groups in phoneRegex.findall(temp):
	phoneNum = '-'.join([groups[0],groups[2],groups[4]])
	print('groups[0] = ' + groups[0])
	print('groups[2] = ' + groups[2])
	print('groups[4] = ' + groups[4])
	if groups[5] != '':
		phoneNum += ' x' + groups[5]
	matches.append(phoneNum)
for groups in mailRegex.findall(temp):
	matches.append(groups)
if len(matches) > 0:
	print('Copied to clipbroad:')
	print('\n'.join(matches))
else:
	print('No phone nunbers or email addresses.')

"""
#phoneResult = phoneRegex.findall(temp) #findall()返回的是一个字符串列表 
for i in range(len(phoneResult)):
	for j in range(len(phoneResult[1])):
		print(phoneResult[i][j], end = '')
	print('')
#print(phoneResult)

mailResult = mailRegex.findall(temp)
for i in range(len(mailResult)):
	print(mailResult[i])
"""