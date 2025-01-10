print("Want to find out what superhereo you are? ")
print("Answer the questions to find out what superhero name is meant for you!")
ans=input("Input guy or girl? :")
if ans == "guy":
    ans = input("Input Fast or fly: ")
    if ans == "fly":
        ans = input("Input Silver or Red: ")
        if ans == "silver":
            print("Congrats your superhero name is Thor!")
        elif ans == "red":
            print("Congrats your superhero name is Super Man!")
    elif ans == "fast":
        ans = input("Input red or green: ")
        if ans == "red":
            print("Congrats your superhero name is The Flash!")
        elif ans == "green":
            print("Congrats your superhero name is Green Lantern!")
elif ans == "girl":
    ans = input("Input Dark or Bright: ")
    if ans == "dark":
        ans = input("Input Bat or Cat: ")
        if ans == "bat":
            print("Congrats your superhero name is Batgirl!")
        elif ans == "cat":
            print("Congrats your superhero name is CatWomen!")
    elif ans == "bright":
        ans = input("Input pink or green: ")
        if ans == "pink":
            print("Congrats your superhero name is Harley Quinn!")
        elif ans == "green":
            print("Congrats your superhero name is She-Hulk!")
