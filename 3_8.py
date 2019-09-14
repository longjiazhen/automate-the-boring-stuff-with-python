import random
print('I am thinking of a number between 1 and 20.')
my_num = random.randint(1, 20)
times = 0
your_num = -1
while your_num != my_num:
    print('Take a guest.')
    your_num = input('> ')
    times += 1
    if int(your_num) < my_num:
        print('Your guess is too low.')
    elif int(your_num) > my_num:
        print('Your guess is too high.')
    else:
        print('Good job! You guessed my number in', times, 'guesses!')
        break
print('Thank you!')

