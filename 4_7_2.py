import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print('spam: ')
print(spam)
print('cheese: ')
print(cheese)

dog = [[1, 2, 3], [11, 22, 33], [111, 222, 333]]
#cat = copy.deepcopy(dog)
cat = copy.copy(dog)
cat[0][0] = 0
print('dog: ')
print(dog)
print('cat: ')
print(cat)

