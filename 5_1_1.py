birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthdays of ' + name)
    else:
        print('I don\'t know the birthday of ' + name)
        print('What\'s his birthday?')
        bday = input()
        birthdays[name] = bday
        print('birthday database updated.')
