allGuests = {'Alice': {'apples': 5, 'milk': 12},
             'Bob': {'egges':3, 'apples': 2},
             'Carol': {'cups': 3, 'pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print('- Apples ' + str(totalBrought(allGuests, 'apples')))
print('- Milk ' + str(totalBrought(allGuests, 'milk')))
print('- Cakes ' + str(totalBrought(allGuests, 'cakes')))
print('- Egges ' + str(totalBrought(allGuests, 'egges')))
print('- Cups ' + str(totalBrought(allGuests, 'cups')))
print('- Pies ' + str(totalBrought(allGuests, 'pies')))

