#Kobe

#Init
import time
import random
Magic_list = ["Yes" , "Definitly" , "Absolutley" , "Sure" , "Of course" , "No" , "Not likely" , "Doubtful" ,"Unlikely" , "No way" , "Maybe" , "Ask again later" , "Cannot predict now" , "Uncertain" , "Try again"]

while 1 == 1 :
    print("Welcome to Magic 8 Ball! ")

    while 1 == 1 :
        question = input("Input a yes or no question. Make sure to include the question mark: ")
        if question.endswith('?'):
            break
        else:
            print("Please make sure your question ends with a question mark.")


    print("shake...")
    time.sleep(2)
    print("shake...")
    time.sleep(2)
    print("shake...")
    time.sleep(2)

    print(random.choice(Magic_list))

    another = int(input(print("Would you like to ask another question? \n 1.)Yes \n 2.)no ")))

    if another == 2 :
        break
