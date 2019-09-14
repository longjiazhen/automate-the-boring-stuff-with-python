#!/usr/bin/env python3
#coding=utf-8
import sys, pyperclip

#保存账号和密码
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
			 'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
			  'luggage': '12345'}

#处理命令行参数
if len(sys.argv) < 2:
	print('Usage: python 6_3.py [account] - copy account password')
	sys.exit()
account = sys.argv[1] #第一行参数是账户名

#复制正确的口令
if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' + account + 'copied to clipboard.')
else:
	print('There is no account named ' + account)



