"""
print('Test1:')
name = ''
while name != 'your name':
    print('Please type your name:')
    name = input('> ')
print('Thank you!')

print('Test2:')
name = ''
while True:
    print('Please type your name:')
    name = input('> ')
    if name == 'your name':
        break
print('Thank you!')

print('Test3:')
name = ''
while True:
    print('Who are you?')
    name = input('> ')
    if name != 'Joe':
        continue
    print('Hello, Joe, what\'s the password?')
    password = input('>')
    if password == '123':
        print('Welcome!')
        break
print('Thank you!')

print('Test4:')
mstr = '我是小可爱'
for i in range(5):
    print('(' + str(i) + ')', mstr)
print('Test5:')
i = 0
while i < 5:
    print('(' + str(i) + ')', mstr)
    i += 1
"""
print('Test6.1:')
for i in range(12, 16):
    print(i)
print('======')
for i in range(0, 10, 2):
    print(i)
print('======')
for i in range(5, 0, -1):
    print(i)
