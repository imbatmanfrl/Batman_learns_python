import random

while True:
    choices = ["rock", "paper", "scissors", "🦇"]

    computer = random.choice(choices)

    player = ""

    # if player == choices:
    # else:
    #    print("you have to pick rock paper or scissors!")

    while player not in choices:
        player = input("rock paper scissors 🦇?").lower()
    print("player: " + player)
    print("computer: " + computer)

    if player == computer:
        print("TIE! let's try again")
    elif player == "rock":
        if computer == "paper":
            print("you loose")
        elif computer == "scissors":
            print("you win")
        elif computer == "🦇":
            print("YOU LOOSE! ")
    elif player == "paper":
        if computer == "rock":
            print("you win")
        elif computer == "scissors":
            print("you loose")
        elif computer == "🦇":
            print("YOU LOOSE! ")
    elif player == "scissors":
        if computer == "paper":
            print("you win")
        elif computer == "rock":
            print("you loose")
        elif computer == "🦇":
            print("YOU LOOSE! ")
    elif player == "🦇":
        if computer == "paper":
            print("YOU WIN!")
        elif computer == "scissors":
            print("YOU WIN!")
        elif computer == "rock":
            print("YOU WIN! ")
    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("bye")




