#kobe Campbell
#1/8/2025
#Multiplication quiz

import random
import time
start_time = time.time()


print("welcome to Multiplication Quiz")#greeting


while 1==1 :#while loop player gets to end whenever they want
    difficulty = int(input("please slecet difficulty 1.)easy 2.)medium 3.)hard 4.)end:"))#Player selects difficulty
    if difficulty == 1 :#difficulty (easy)

        questions = int(input("How many questions would you like? :"))#player chooses amount of questions they want
        correct = 0
        start = time.time()#timer starts
        for i in range (questions) :#asking questions
            num1 = random.randint(1,5)
            num2 = random.randint(1,5)
            answer = int(input( " What is " + str(num1) + " x " + str(num2) +" :" ))
            if answer == num1*num2 :
                print("Correct!")
                correct = correct + 1
            else :
                print("Incorrect.")
        print("Congrats you got " + str(correct) + " out of " + str(questions) + " right!" )#congradulates player when finished
        end = time.time()
        print("You took " + str(end - start) + "to finish")#time it took player to finish all questions 


    if difficulty == 2 :

        questions = int(input("How many questions would you like? :"))
        correct = 0
        start = time.time()
        for i in range (questions) :
            num1 = random.randint(1,10)
            num2 = random.randint(1,10)
            answer = int(input( " What is " + str(num1) + " x " + str(num2) +" :" ))
            if answer == num1*num2 :
                print("Correct!")
                correct = correct + 1
            else :
                print("Incorrect.")
        print("Congrats you got " + str(correct) + " out of " + str(questions) + " right!" )
        end = time.time()
        print("You took " + str(end - start) + "to finish")


    if difficulty == 3 :

        questions = int(input("How many questions would you like? :"))
        correct = 0
        start = time.time()
        for i in range (questions) :
            num1 = random.randint(1,15)
            num2 = random.randint(1,15)
            answer = int(input( " What is " + str(num1) + " x " + str(num2) +" :" ))
            if answer == num1*num2 :
                print("Correct!")
                correct = correct + 1
            else :
                print("Incorrect.")
        print("Congrats you got " + str(correct) + " out of " + str(questions) + " right!" )
        end = time.time()
        print("You took " + str(end - start) + "to finish")


    if difficulty == 4 :
        break

