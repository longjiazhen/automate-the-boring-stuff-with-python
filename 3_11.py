def collatz(number):
    if number % 2 == 0:
        number = int(number/2)
        print(number)
    else:
        number = 3 * number + 1
        print(number)
    return number
print('Enter a number')
try:
    num = int(input('> '))
    while num != 1:
        num = collatz(num)
except ValueError:
    print('Please enter an interger.')
print('Thank you!')

        
