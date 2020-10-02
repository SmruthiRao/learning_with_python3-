import random
rng = random.Random()
number = rng.randrange(1, 100)

guesses = 0
msg = ' '

while True:
    guess = int(input(msg+'\n Guess a number between 1 and 100:'))
    guesses += 1
    if guess > number:
        msg += str(guess) + " is higher than the number to be guessed \n"
    elif guess < number:
        msg += str(guess) + "is lower than the number to be guessed \n"
    else:
        break


print("number of guesses to find number", number, "is : ", guesses)
input("\n\nGreat, you got it in {0} guesses!\n\n".format(guesses))
