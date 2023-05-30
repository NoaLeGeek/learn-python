import random

import Utils
# Speedrun getting cancer

# Guess the number
def guess_number() -> None:
    minimum = 0
    maximum = 0
    tries = 0
    menu = {0: "CUSTOM MODE: Guess the number with your settings",
            1: "CUSTOM MODE WITH TRIES: Guess the number with your settings and your tries",
            2: "1MILLION MODE: Guess the number between 1 and 1.000.000",
            3: "1BILLION MODE: Guess the number between 1, and 1.000.000.000",
            4: "1MILLION MODE WITH TRIES: Guess the number between 1 and 1.000.000 with 30 tries",
            5: "1BILLION MODE WITH TRIES: Guess the number between 1, and 1.000.000.000 with 45 tries"}
    match (int(input("Choose your mode!\n" + Utils.generate_choices(menu)))):
        case 0:
            minimum = int(input("I'm thinking of a number between [?] and ... included."))
            maximum = int(input("I'm thinking of a number between" + str(minimum) + "and ... included."))
            if minimum == maximum:
                print("The minimum and maximum values should not be the same.")
                return
        case 1:
            minimum = int(input("I'm thinking of a number between [?] and ... included. You have ... tries."))
            maximum = int(input("I'm thinking of a number between " + str(minimum) + " and [?] included."))
            tries = int(input("I'm thinking of a number between " + str(minimum) + " and " + str(
                maximum) + "included. You have [?] tries."))
            if minimum == maximum:
                print("The minimum and maximum values should not be the same.")
                return
        case 2:
            minimum = 1
            maximum = 1000000
        case 3:
            minimum = 1
            maximum = 1000000000
        case 4:
            minimum = 1
            maximum = 1000000
            tries = 30
        case 5:
            minimum = 1
            maximum = 1000000000
            tries = 45
    if minimum > maximum:
        swap = maximum
        maximum = minimum
        minimum = swap
    if tries != 0:
        number = random.randint(minimum, maximum)
        guess = maximum + 1
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
    else:
        number = random.randint(minimum, maximum)
        guess = maximum + 1
        print("I'm thinking of a number between", minimum, "and", str(maximum) + ".")
        while guess != number:
            guess = int(input("Guess the number!\n"))
            if guess == number:
                print("You guessed it!")
                break
            elif guess < number:
                print("It's more!")
            elif guess > number:
                print("It's less!")


# Plays rock, paper, scissors
def rock_paper_scissors() -> None:
    choices = {0: "Rock", 1: "Paper", 2: "Scissors"}
    choice = 3
    while choice > 2 or choice < 0:
        choice = int(input("Rock, Paper, Scissors: Choose!\n" + Utils.generate_choices(choices)))
        if choice < 3:
            break
        print("Invalid choice. You can only choose 0, 1 or 2.")
    computer = random.randint(0, 2)
    if choice == computer:
        replay = int(input("It's a tie!\nWants to replay?\n" + Utils.generate_choices({0: "Yes", 1: "No"})))
        if replay == 0:
            rock_paper_scissors()
    # You win
    elif (choice == 0 and computer == 2) or (choice == 1 and computer == 0) or (choice == 2 and computer == 1):
        replay = int(input(
            "The computer chose " + choices[computer] + "\nYou win!\nWants to replay?\n" + Utils.generate_choices(
                {0: "Yes", 1: "No"})))
        if replay == 0:
            rock_paper_scissors()
    # You lose
    else:
        replay = int(input(
            "The computer chose " + choices[computer] + "\nYou lose!\nWants to replay?\n" + Utils.generate_choices(
                {0: "Yes", 1: "No"})))
        if replay == 0:
            rock_paper_scissors()
