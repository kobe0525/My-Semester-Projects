#Kobe
#Simple calculator

#init


#functions

#This Function adds num1 with num2 and print result
def addition (num1,num2):
    result= num1 + num2
    print ("The Result is: " + str(result))

#This function subtracts Num1 with num2 and print result
def subtract (num1,num2):
    result=num1 - num2
    print ("The Result is: " + str(result))
#This function multiplies num1 with num2 and prints result
def multiply (num1,num2):
    result=num1*num2
    print ("The Result is: " + str(result))
#This function divides num1 with num2 and prints result
def divide(num1,num2):
    result=num1/num2
    print ("The Result is: " + str(result))


def calculator():
    print("Welcome to simple calculator")

    while 1==1:
        print("Please choose an operation: ")
        print("""
        1. Addition
        2.Subtraction
        3.Multiplication
        4.Division.
        5.Quit""")
        option=int(input("(1-5)Select option: "))

        if option == 1:
            int1=int(input("what is the first number you would like to add"))
            int2=int(input("What is the secound number you would like to add"))
            addition(int1,int2)

        if option == 2:
            int1=int(input("what is the first number you would like to subtract"))
            int2=int(input("What is the secound number you would like to subtract"))
            subtract(int1,int2)


        if option == 3:
            int1=int(input("what is the first number you would like to multiply"))
            int2=int(input("What is the secound number you would like to multiply"))
            multiply(int1,int2)



        if option == 4:
            int1=int(input("what is the first number you would like to divide"))
            int2=int(input("What is the secound number you would like to divide"))
            divide(int1,int2)



        if option == 5:
            break

#main
calculator()
