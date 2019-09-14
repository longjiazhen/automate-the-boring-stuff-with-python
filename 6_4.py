#!/usr/bin/env python3
#在一个无序列表的每一行前面加上* 
"""
假设先在剪贴板拷贝：
Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars
"""

#1.从剪贴板复制文本
import pyperclip
text = pyperclip.paste()
#此时text == 'Lists of animals\nLists of aquarium life\nLists of biologists by author abbreviation\nLists of cultivars'
#text = 'Lists of animals\nLists of aquarium life\nLists of biologists by author abbreviation\nLists of cultivars'

#2.分行，并将每一行前面加上*
lines = text.split('\n')
#此时lines == ['Lists of animals', 'Lists of aquarium life', 'Lists of biologists by author abbreviation', 'Lists of cultivars']
for i in range(len(lines)):
	lines[i] = '*' + lines[i]
text = '\n'.join(lines)

#3.将新的文本复制到剪贴板
pyperclip.copy(text)


