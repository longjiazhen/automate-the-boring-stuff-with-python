#!/usr/bin/env python3
#打印结果需将行列倒置并对齐
tableData = [['apples', 'oranges', 'cherries', 'banana'], 
			 ['Alice', 'Bob', 'Carol', 'David'],
			 ['dogs', 'cats', 'moose', 'goose']] 
oriRow = len(tableData) #行
oriColumn = len(tableData[0]) #列
colWidths = [0] * oriRow #初始化，每一列的宽度均为0

#计算每一列的宽度
for i in range(oriRow):
	maxWidth = len(tableData[i][0])
	for j in range(oriColumn):
		if len(tableData[i][j]) > maxWidth:
			maxWidth = len(tableData[i][j])
	colWidths[i] = maxWidth
#print(colWidths) #[8, 5, 5]


#行列倒置，并且第一列右对齐，其余列左对齐
def printTable(table):
	for j in range(len(table[0])):
		for i in range(len(table)):
			if i == 0:
				print(table[i][j].rjust(colWidths[0]), end = ' ')
			else:
				print(table[i][j].ljust(colWidths[i]), end = ' ')
		print('')

printTable(tableData)


