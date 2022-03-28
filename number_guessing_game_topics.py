# Number Guessing Game Topics:
#   - Print Statement
#   - Variables
#   - User Input
#   - If Statements and Boolean Operators
#   - While Loops
#   - Try/Except
#   - Random Numbers

# PRINT STATEMENT:
# print('hello world')
#
# age = 7
# print('I am 7 years old')
# print('I am ' + str(age) + ' years old.')
# print('I am', str(age), 'years old.')
# print(f'I am {age} years old.')
#
# print('It\'s a Tuesday.')
# print("It's a Tuesday.")
# print('random\ntext')

# VARIABLES:
# x = 4
# y = x + 1
# print(y)
#
# count = 0
# count += 1
# print(count)

# USER INPUT:
# number = input('Enter a number: ')
# print('Your number is', number)

# IF STATEMENTS AND BOOLEAN OPERATORS:
# is_raining = True
# is_cold = False
#
# if is_raining:
#     print('It is raining.')
# else:
#     print('It is not raining.')
#
# if is_raining or is_cold:
#     print('It is either raining or cold. It could also be both raining and cold.')
# else:
#     print('It is neither raining nor cold.')
#
# if is_raining and is_cold:
#     print('It is both raining and cold.')
# else:
#     print('It is either raining or cold (not both). It could also be neither raining nor cold.')
#
# grade = 94
# if grade >= 90:
#     letter_grade = 'A'
# elif grade >= 80:
#     letter_grade = 'B'
# elif grade >= 70:
#     letter_grade = 'C'
# else:
#     letter_grade='F'
# print(letter_grade)

# WHILE LOOPS:
# i = 1
# while i < 6:
#   print(i)
#   i += 1
#
# while True:
#   x = input('Enter anything: ')
#   if x == 'stop':
#       break

# TRY/EXCEPT:
# try:
#   print(x)
# except:
#   print('An exception occurred.')
#
# number = 'hello'
# try:
#   number = int('hello')
# except ValueError:
#   print('Invalid input.')

# RANDOM NUMBERS:
# import random
# Return a random integer N such that a <= N <= b (from a to b inclusive)
# random.randint(a, b)
# print(random.randint(1,10))

# Modifications:
#   - Add fancy ASCII text to make the game more visually appealing
#   - Make an easy, medium, and hard level that the player can choose from with different ranges and turns.
#   - Make the game for two players where the winner is the player who guesses the number first
