def mFunction(mList):
    mStr = ''
    for i in mList:
        if i == mList[0]:
            mStr = '\'' + str(i) + ', '
        elif i != mList[-1]:
            mStr = mStr + str(i) + ', '
        else:
            mStr = mStr + str(i) + '\''
    return mStr
spam = ['apples', 'bananas', 'tofu', 'cats']
print(mFunction(spam))
temp = [1, 'a', 2, 'B']
print(mFunction(temp))
