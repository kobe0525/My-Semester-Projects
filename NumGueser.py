import random

Level = int(input("This is the guessing game! Would you like to play on easy(1) medium(2)or hard(3):"))

if Level == 1:#easy level
    guess = int(input("You have 3 tries to guess the right number. Enter Number 0-5 :"))

    answer = random.randint(0,5)

    if guess == answer:
       print("You are correct!")
    else:
        if guess>answer:
            print("too high")
        if guess<answer:
            print("Too low")
    guessTwo= int(input("Guess again:"))
    if guessTwo == answer:
       print("You are correct!")
    else:
        if guessTwo>answer:
            print("too high")
        if guessTwo<answer:
            print("Too low")
    guessThree= int(input("Guess again:"))
    if guessThree == answer:
        print("you are correct!!")
    else :
        print("You lose")



if Level == 2:#Medium level
    guess = int(input("You have 3 tries to guess the right number. Enter Number 0-10 :"))

    answer = random.randint(0,10)

    if guess == answer:
       print("You are correct!")
    else:
        if guess>answer:
            print("too high")
        if guess<answer:
            print("Too low")
    guessTwo= int(input("Guess again:"))
    if guessTwo == answer:
       print("You are correct!")
    else:
        if guessTwo>answer:
            print("too high")
        if guessTwo<answer:
            print("Too low")
    guessThree= int(input("Guess again:"))
    if guessThree == answer:
        print("you are correct!!")
    else :
        print("You lose")




if Level == 3:#Medium level
    guess = int(input("You have 3 tries to guess the right number. Enter Number 0-15 :"))

    answer = random.randint(0,15)

    if guess == answer:
       print("You are correct!")
    else:
        if guess>answer:
            print("too high")
        if guess<answer:
            print("Too low")
    guessTwo= int(input("Guess again:"))
    if guessTwo == answer:
       print("You are correct!")
    else:
        if guessTwo>answer:
            print("too high")
        if guessTwo<answer:
            print("Too low")
    guessThree= int(input("Guess again:"))
    if guessThree == answer:
        print("you are correct!!")
    else :
        print("You lose")
