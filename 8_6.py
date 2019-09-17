#!/usr/bin/env python3

"""
多重剪贴板
该程序将利用一个关键字保存每段剪贴板文本。
例如，当运行 py mcb.pyw save spam，剪贴板中当前的内容就用关键字 spam 保存。
通过运行 py mcb.pyw spam，这 段文本稍后将重新加载到剪贴板中。
如果用户忘记了都有哪些关键字，他们可以运 行 py mcb.pyw list，将所有关键字的列表复制到剪贴板中
下面是程序要做的事: 
针对要检查的关键字，提供命令行参数。
如果参数是 save，那么将剪贴板的内容保存到关键字。 
如果参数是 list，就将所有的关键字拷贝到剪贴板。 否则，就将关键词对应的文本拷贝到剪贴板。
这意味着代码需要做下列事情: 
从 sys.argv 读取命令行参数。 读写剪贴板。
保存并加载 shelf 文件。
"""

# 拷贝和粘贴需要pyperclip，读取命令行参数需要sys
# 当用户希望保存一段剪贴板文本时，保存在shelf文件中；当用户希望将文本拷贝回剪贴板时，打开shelf文件
import shelve, pyperclip, sys

#处理命令行参数
if len(sys.argv) < 2:
	print("""Usage:\tpython 8_6.py save <keyword> - Saves clipboard to keyword.
	python 8_6.py <keyword> - Loads keyword to clipboard.
	python 8_6.py list - Loads all keywords to clipboard.""")
	sys.exit()

mcbShelf = shelve.open('mcb')
# py mcb.pyw save spam
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
# py mcb.pyw list 或者 py mcb.pyw spam
elif len(sys.argv) == 2:
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])


mcbShelf.close()


