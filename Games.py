import random
import Utils


# Guess the number
def guess_number(minimum: int = 1, maximum: int = 100, tries: int = 3) -> None:
    if minimum == maximum:
        print("The minimum and maximum values should not be the same.")
    else:
        if minimum > maximum:
            swap = maximum
            maximum = minimum
            minimum = swap
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


# Plays rock, paper, scissors
def rock_paper_scissors() -> None:
    lizt = {0: "Rock", 1: "Paper", 2: "Scissors"}
    choice = 3
    while choice > 2 or choice < 0:
        choice = int(input("Rock, Paper, Scissors: Choose!\n" + Utils.generate_choices(lizt)))
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
        replay = int(input("The computer chose " + lizt[computer] + "\nYou win!\nWants to replay?\n" + Utils.generate_choices({0: "Yes", 1: "No"})))
        if replay == 0:
            rock_paper_scissors()
    # You lose
    else:
        replay = int(input("The computer chose " + lizt[computer] + "\nYou lose!\nWants to replay?\n" + Utils.generate_choices({0: "Yes", 1: "No"})))
        if replay == 0:
            rock_paper_scissors()
