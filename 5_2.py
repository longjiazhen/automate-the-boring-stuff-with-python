#计算一个字符串中每个字符出现的次数
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count) #打印到屏幕上，键值按ASCII码排序
print(pprint.pformat(count)) #与上一句等价，即pprint.pformat(count)得字符串
