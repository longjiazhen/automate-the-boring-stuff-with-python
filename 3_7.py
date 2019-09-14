print('Test1:')
def spam(devideBy):
    try:
        return 42 / devideBy
    except ZeroDivisionError:
        print('Error, can\'t not devide zero.')
print(spam(2)) # 21.0
print(spam(12)) # 3.5
print(spam(0)) # Error, can't not devide zero.然后输出None
print(spam(1)) #42.0
print('Test2:')
def spam(devideBy):
        return 42 / devideBy
try:
    print(spam(2)) # 21.0
    print(spam(12)) # 3.5
    print(spam(0)) # Error, can't not devide zero.然后就不执行了
    print(spam(1))
except ZeroDivisionError:
    print('Error, can\'t not devide zero.')

#因为一跳到except语句，就不会再回到try里面继续执行了
