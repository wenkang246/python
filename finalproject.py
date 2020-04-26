import random

#rock paper scissors
def RPS():
    plays = ["Rock", "Paper", "Scissors"]
    computer = plays[random.randint(0,2)]
    player = input("Rock, Paper, or Scissors? ")
    if player.casefold() == computer.casefold():
        print("Tie!")
    elif player.casefold() != plays[1].casefold():
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player.casefold() == plays[2].casefold():
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player.casefold() == plays[3].casefold():
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")

RPS()





# Guess the number
def guessNum():
    num = random.randint(1, 100)
    guess = int(input("Enter a whole number from 1 to 100: "))
    while num != "guess":
        if guess < num:
            print("Too low")
            guess = int(input("Try again: "))
        elif guess > num:
            print("Too high")
            guess = int(input("Try again: "))
        else:
            print("You got it!")
            break

guessNum()
