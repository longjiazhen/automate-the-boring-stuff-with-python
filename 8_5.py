#！/usr/bin/env python3
#coding:utf-8

"""
下面是程序所做的事:
创建 35 份不同的测验试卷。
为每份试卷创建 50 个多重选择题，次序随机。
为每个问题提供一个正确答案和 3 个随机的错误答案，次序随机。 
将测验试卷写到 35 个文本文件中。
将答案写到 35 个文本文件中。
这意味着代码需要做下面的事: 
将州和它们的首府保存在一个字典中。 
针对测验文本文件和答案文本文件，调用 open()、write()和 close()。 
利用 random.shuffle()随机调整问题和多重选项的次序。
"""

import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 
'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 
'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 
'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 
'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 
'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 
'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 
'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 
'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 
'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# 循环35次，每次只考虑一份测试试卷
for quizNum in range(35):
	# 创建试题文件和答案文件
	quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
	answerKeyFile = open('capitalsquiz_answer%s.txt' % (quizNum + 1), 'w')
	# 写试题头部
	quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
	quizFile.write((' ' * 20) + 'State Capitals Quiz (Forms %s)' % (quizNum + 1))
	quizFile.write('\n\n')
	# 写试题的题目
	states = list(capitals.keys())
	# shuffle() 方法将序列的所有元素随机排序
	random.shuffle(states)
	# 写试题的答案选项
	for questionNum in range(50):
		correctAnswer = capitals[states[questionNum]]
		wrongAnswers = list(capitals.values())
		# del 列表名[下标] 可以直接删除列表里的某一项
		del wrongAnswers[wrongAnswers.index(correctAnswer)]
		# random.sample() 第一个参数是提供选择的列表，第二个参数表示从这个列表中取多少个随机且不相同的元素
		wrongAnswers = random.sample(wrongAnswers, 3)
		# wrongAnswers 是一个列表，所以写成 + [correctAnswer]，这里是列表相加
		answerOptions = wrongAnswers + [correctAnswer]
		random.shuffle(answerOptions)
		# 将题目和选项写入文件
		quizFile.write('%s. What is the capital of %s?\n' % 
			(questionNum + 1, states[questionNum]))
		for i in range(4):
			quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
		quizFile.write('\n')
		# 将答案写入文件
		answerKeyFile.write('%s. %s\n' % (questionNum + 1, 
			'ABCD'[answerOptions.index(correctAnswer)]))
	quizFile.close()
	answerKeyFile.close()




