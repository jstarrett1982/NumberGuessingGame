# Jackie Starrett
# Making a Game: guess the number between 1 and 100

# This library allows us to generate random numbers
import random

# This function generates a random integer between 1 and 100 (inclusive), and assigns it to the variable secretNum
secretNum = random.randint(1, 100)

# This variable will get put into the loop and keep track of the number of guesses.
numGuesses = 1

# This allows the user to guess a number according to the parameters listed and assigns it to the guess variable
guess = eval(input("guess a number between 1 and 100, 666 quits   "))
print()

# The while loop evaluates the user's guess and returns a response of whether the guess is higher or lower than the secretNum
# The loop is broken if the value for the secretNum is entered by the user, or if the quit number, 666, is entered.
# The loop can also end if a number less than one or greater than 100 is entered, triggering the else condition.
# While in the loop, each time a valid number is guessed, the value for numGuesses increases by 1.
while 1 <= guess <= 100:
    if guess == secretNum:
        break
    if guess == 666:
        break
    elif guess < secretNum:
        print("your answer is LOWER than the secret number   ")
        print()
        guess = eval(input("guess again  "))
        print()
        numGuesses = numGuesses + 1
    elif guess > secretNum:
        print("your answer is HIGHER than the secret number   ")
        print()
        guess = eval(input("guess again   "))
        print()
        numGuesses = numGuesses + 1

# When a number below one or greater than 100 is entered, the conditions of the while loop are not met, so this else statement below fires.
# This statement also prints when the quit number, 666, is entered, since it is above 100.
else:
    print("invalid number")

# When the correct number is entered in the loop, the loop breaks to the statement below, and this response is printed.
if guess == secretNum:
    print("CONGRATULATIONS you guessed the number in", numGuesses, "guesses")

# When the quit value is entered by the user, the loop breaks to the statement below and this response is given.
if guess == 666:
    print("looks like you gave up")
