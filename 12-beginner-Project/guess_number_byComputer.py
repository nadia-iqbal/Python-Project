import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' and low != high:
            guess = random.randint(low, high)
            feedback = input(f'Is {guess} too high(H), too low(L), or correct(C)??').lower()
            if feedback =='h':
              high = guess - 1
            elif feedback =='l':
              low = guess + 1
    print(f'Yay, The computer guess your number, {guess -1} correctly!')
computer_guess(100)
