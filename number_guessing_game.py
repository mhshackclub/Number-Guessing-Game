# Player guesses a number within a certain range and tries to match the computer-generated random number within a given number of turns

# Imports random package that provides tools for random functions
import random

# Asks user to enter the lowest and highest bounds for the random number and checks input
is_int = False
while not is_int:
    lower_bound = input('Enter the lowest possible number that can be guessed: ')
    upper_bound = input('Enter the highest possible number that can be guessed: ')
    try:
        lower_bound = int(lower_bound)
        upper_bound = int(upper_bound)
        is_int = True
    except ValueError:
        print('Invalid input. You must enter an integer for both the lower bound and upper bound.')

# Generates the random number
rand_num = random.randint(lower_bound, upper_bound)

# Initializes variables for setting and tracking the number of turns
num_turns = 8
turn = 1
print('\nYou have', num_turns, 'turns.\n')

# Asks user to guess number until turns run out or correct number is guessed
while True:
    # Prints out what the current turn is
    print(f'This is turn {turn}')

    # Asks user to input a number to guess and checks input
    is_valid = False
    while not is_valid:
        guess_num = input(f'Enter a number from {lower_bound} to {upper_bound}: ')
        try:
            guess_num = int(guess_num)
            if guess_num in range(lower_bound, upper_bound + 1):
                is_valid = True
            else:
                print('Invalid input. You must enter an integer within the given range.')
        except ValueError:
            print('Invalid input. You must enter an integer within the given range.')

    # Checks how the guessed number compares with the actual generated number
    if rand_num == guess_num:
        print('You win! Great job!\n')
        break
    elif rand_num > guess_num:
        print('Your guess is too low. Higher next time!\n')
    else:
        print('Your guess is too high. Lower next time!\n')

    # Checks whether the user ran out of turns
    if turn >= num_turns:
        print('You ran out of turns!')
        break

    # Increments the number of turns
    turn += 1

print('Game over!')
print('The winning number was', str(rand_num) + '.')
