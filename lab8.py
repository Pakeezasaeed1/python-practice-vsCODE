import random
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
number=random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess=input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("you guess the {}. That is correct! you win!".format(guess))
        isGuessRight=True
    else:
        print("you guessed {}. Sorry, that is not correct. Try Again.".format(guess))