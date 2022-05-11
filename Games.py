import random


# Guess the number
def guess_number(minimum: int = 1, maximum: int = 100, tries: int = 3) -> None:
    if minimum == maximum:
        print("The minimum and maximum values should not be the same.")
    elif minimum > maximum:
        print("The minimum value should be smaller than the maximum value.")
    else:
        number = random.randint(minimum, maximum)
        guess = 0
        print("I'm thinking of a number between", minimum, "and", str(maximum) + ". You have", tries, "tries.")
        while guess != number:
            if tries == 0:
                print("You lost. The number was:", number)
                break
            guess = int(input("Guess the number!\n"))
            if guess == number:
                print("You guessed it!")
                break
            elif guess < number:
                print("It's more!")
            elif guess > number:
                print("It's less!")
            tries -= 1
