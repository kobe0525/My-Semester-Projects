#Kobe
#Pokemon evolution game
#11/21/2024

#initilize
import random


#global variable
pokemon_level = 0
pokemon_name = "charmander"
battle_wins = 0
battle_losses = 0
#Functions

def draw_charmander():
    print("""⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬛🟧🟧🟧🟧⬛⬜⬜⬜⬜⬜⬜⬜
    ⬜⬛🟧🟧🟧🟧🟧🟧⬛⬜⬜⬜⬜⬜⬜
    ⬜⬛🟧🟧🟧🟧🟧🟧⬛⬜⬜⬜🟥⬜⬜
    ⬜⬛🟦🟧🟧🟧🟧🟦⬛⬜⬜🟥🟥🟥⬜
    ⬛⬜🟦🟧🟧🟧🟧🟦⬜⬛⬜🟥🟥🟥⬜
    ⬛⬜🟦🟧🟧🟧🟧🟦⬜⬛🟥🟥🟨🟥⬜
    ⬛🟧🟧🟧🟧🟧🟧🟧🟧⬛🟥🟨🟨🟥🟥
    ⬜⬛🟧🟧🟧🟧🟧🟧⬛⬜⬜⬛🟨🟥🟥
    ⬛🟧⬛⬛⬛⬛⬛⬛🟧⬛⬜⬛🟧⬛⬜
    ⬛🟧⬛🟧🟧🟧🟧⬛🟧⬛⬛🟧🟧⬛⬜
    ⬜⬛🟧🟧🏻🏻🟧🟧⬛🟧🟧🟧⬛⬜⬜
    ⬜⬛🟧🏻🏻🏻🏻🟧⬛🟧🟧🟧⬛⬜⬜
    ⬜⬛🟧🏻🏻🏻🏻🟧⬛🟧⬛⬛⬜⬜⬜
    ⬛🟧⬛⬛⬛⬛⬛⬛🟧⬛⬜⬜⬜⬜⬜
    ⬛⬛⬛⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜       """)

def draw_charmeleon():
    print("""⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬛🟥⬛⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬛🟥🟥⬛⬜⬜⬛🟥🟥⬛⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬛🟥🟥🟥⬛⬜⬜⬛🟥🟥🟥⬛⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬛🟥🟥🟥⬛⬜⬜⬜⬛🟥🟥⬛⬛⬛⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬛🟨🟥⬛⬜⬜⬜⬛⬛🟥🟥⬛🟥⬛⬜⬜⬜
    ⬜⬜⬜⬛⬛🟥🟨⬛⬜⬜⬜⬛🟥🟥🟥🟥🟥🟥🟥⬛⬜⬜
    ⬜⬜⬛⬛🟥🟥⬛⬜⬜⬜⬛🟥🟥🟥🟥🟥🟥🟥🟥⬛⬜⬜
    ⬜⬛🟥🟥🟥⬛⬜⬜⬜⬜⬛🟥🟥🟥⬛🟥🟥🟥🟥🟥⬛⬜
    ⬛🟥🟥🟥⬛⬜⬜⬜⬜⬛⬛🟥🟥🟥⬜⬛🟥🟥🟥🟥🟥⬛
    ⬛🟥🟥🟥⬛⬜⬜⬛⬛🟥🟥⬛🟥⬛⬜⬛⬛🟥🟥🟥🟥⬛
    ⬛🟥🟥🟥🟥⬛⬛🟥🟥🟥🟥🟥🟥⬛🟥🟥🟥🟥🟥🟥⬛⬜
    ⬛⬛🟥🟥🟥⬛🟥🟥🟥⬛🟥🟥🟥🟥⬛🟥🟥🟥⬛⬛⬜⬜
    ⬜⬛🟥🟥🟥🟥🟥⬛🟥⬛🟥🟥🏻🏻⬛⬛⬛⬛🟥🟥⬛⬜
    ⬜⬜⬛🟥⬛🟥🟥⬛🟥⬜⬛🏻🏻🏻⬛⬜⬜⬛🟥🟥⬜⬛
    ⬜⬜⬜⬛⬛🟥🟥⬛🟥🟥🟥⬛🏻⬛⬜⬜⬜⬜⬛⬜🟥⬛
    ⬜⬜⬜⬜⬛🟥🟥🟥⬛🟥⬜⬛🏻⬛⬛⬜⬜⬜⬜⬛⬛⬜
    ⬜⬜⬜⬜⬛⬛🟥🟥🟥⬛⬛🏻⬛🟥⬜⬛⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬛🟥🟥🟥🟥⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬛⬛🟥⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬛⬜🟥⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜""")

def draw_charzard():
    print("""⬜⬜⬜⬜🟥🟥🟥🟨🟨🟨🟨🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜🟥🟥🟥🟨🟥🟨🟥⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜🟧⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜🟥🟥🟧🟥🟨🟨⬜⬛🟧🟧🟧⬛⬜⬜⬜⬜⬜⬜🟧⬜⬜⬜⬜⬜
    ⬜⬜⬜⬜⬜⬜🟧🟧⬜🟥⬜⬜⬜🟥⬜🟧⬛⬜⬜⬜⬜⬜⬜🟧🟧🟧⬜⬜⬜
    ⬜⬜⬜⬜🟧🟧🟧🟧⬜⬜🟥⬜⬛🟥🟥🟥🟧⬛⬜⬜⬜⬜⬜🟧🟧🟧🟧⬜⬜
    ⬜⬜⬜🟧🟧🟧🟧⬜⬜⬜⬜⬜⬜⬛🟥🟥🟧⬛⬛⬜⬜⬜⬜🟧🟦🟧🟧🟧⬜
    ⬜⬜⬜🟧🟧🟦🟧⬜⬜⬜⬜🏻🏻🏻🟥🟫🟧⬜⬛⬜⬜⬜🟧🟧🟦🟦🟦🟧⬜
    ⬜⬜🟧🟧🟦🟦🟧🟧⬜⬜⬜⬛🟪🏻🏻🟫🟧🟧🟧⬛⬜⬜🟧🟦🟦🟦🟦🟧🟧
    ⬜⬜🟧🟦🟦🟦🟧🟧⬜⬜⬛🟧⬛⬛⬛🟧🟧⬛🟧⬛⬜🟧🟧🟦🟦🟦🟦🟦🟧
    ⬜🟧🟧🟦🟦🟦🟧🟧⬜⬜⬜⬛🟧🟧🟧🟧⬛⬛🟧🟧⬛🟧🟧🟦🟦🟦🟥🟦🟧
    ⬜🟧🟦🟦🟦🟦🟧🟧⬜⬜⬜⬜⬛⬛⬛🟧⬛⬜⬛⬛⬛🟧🟦🟦🟥🟥🟦🟦🟧
    🟧🟧🟦🟦🟦🟦🟦🟧🟧⬜⬜⬜⬛🟧🟧🟧⬛⬜⬜⬜🟧🟧🟦🟦🟥🟨🟦🟦🟥
    🟧🟦🟦🟦🟦🟦🟦🟧🟧🟧⬜⬜⬛🟧🟧🟧⬛⬜⬜🟧🟧🟦🟦🟥🟥🟦🟥🟥🟥
    🟧🟦🟦🟦🟦🟦🟦🟦🟧🟧🟧⬜⬛🟧🟧🟧⬛⬜🟧🟧🟧🟦🟦🟥🟨🟥🟨🟥🟧
    🟧🟦🟦⬛⬜⬛🟦🟦🟦🟧🟧⬛🟧🟧🟧🟧⬛🟧🟧🟧🟦🟦🟦🟥🟨🟨🟥🟧🟥
    🟧🟦⬜⬜🟧⬜⬛🟦🟦🟧⬛🟧🟧🟧🟧🟧🟧⬛🟧🟧🟦🟦🟥🟨🟨🟨🟨🟥🟧
    🟧⬜⬜⬛🟧🟧⬛🟦🟦⬛🟧🟧🟧🟧🟧🟧🟧⬛🟧🟦⬜⬜⬛🟥🟧🟨🟨🟧🟥
    🟧⬜⬜⬜⬛🟧🟧⬛⬛🟧🟧🏻🏻🏻🏻🟧🟧🟧⬛🟦⬛🟧⬜🟥🟥🟧🟨🟨🟥
    ⬜⬜⬜⬜⬜⬛🟧🟧🟧⬛🏻🏻🏻🏻🏻🏻🟧🟧🟧⬛🟧🟧⬛🟦⬛🟧⬛🟥🟦
    ⬜⬜⬜⬜⬛⬛⬛⬛⬛🏻🏻🏻🏻🏻🏻🏻🟧⬛🟧🟧🟧⬛🟦⬜⬛🟧⬛⬜🟦
    ⬜⬜⬛⬛🟧🟧🟧🟧⬛🏻🏻🏻🏻🏻🏻🏻🏻🟧⬛⬛⬛🟦⬜⬛🟧🟧⬛⬜⬜
    ⬜⬛🟧🟧🟧🟧⬛⬛⬛🏻🏻🏻🏻🏻🏻🏻🏻🟧⬛🟧🟧⬛⬛🟧🟧⬛⬜⬜⬜
    ⬜⬛🟧🟧🟧⬛🟧🟧⬛🏻🏻🏻🏻🏻🏻🏻🏻🟧🟧⬛🟧🟧🟧🟧⬛⬜⬜⬜⬜
    ⬜⬛🟧🟧⬛🟧🟧🟧⬛🏻🏻🏻🏻🏻🏻🏻🏻🟧🟧🟧⬛🟧🟧⬛⬜⬜⬜⬜⬜
    ⬜⬛🏻🟧⬛🟧🟧🟧🟧⬛🏻🏻🏻🏻🏻🏻🏻🟧🟧🟧🟧⬛⬛⬜⬜⬜⬜⬜⬜
    ⬜⬛🏻🏻🏻⬛🟧🟧🟧🟧⬛🏻🏻🏻🏻🏻⬛🟧🟧🟧🟧⬛⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬛⬛⬛⬛🟧🟧🟧⬛🏻⬛⬛⬛⬛⬛🟧🟧🟧🟧⬛⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬛⬜🟧🟧🟧🟧⬛🏻🏻🏻⬛⬜⬜⬜⬛🟧🟧🟧🟧⬜⬜⬜⬜⬜⬜⬜⬜
    ⬜⬜⬜⬛⬜⬛⬜⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬛⬜⬛⬜⬛⬜⬜⬜⬜⬜⬜⬜          """)

def evolve():#need to add into game
    if pokemon_level ==5 :
        pokemon_name = "charmeleon"
        print("Congrats you evolded from charmander into charmeleon")
        draw_charmeleon()
    elif pokemon_level == 10:
        pokemon_name = "charzard"
        print("Congrats you are evolved from charmeleon into charzard")
        draw_charzard()

def game():
    global battle_losses
    global battle_wins
    global pokemon_name
    global pokemon_level
    print("Welcome to pokemon evolution")
    while 1==1:
        print("Choose today's activity: ")
        activity = input("""1. Train
        2.Gym battle
        3.Rest (Display info)
        4.Quit
        : """)

        if activity == '1':
            print("What would you like to train today?")
            train = int(input("""(1)Attacking
        (2)Defending
            """))

            if train == 1:
                if pokemon_level <= 10:
                    print("Great attacking out there! I can see you are still learning.")
                    pokemon_level = pokemon_level + 1
                    print("Hey, looks like you leveled up! Your current level is " + str(pokemon_level))
                    evolve()

                elif pokemon_level <= 20 and pokemon_level > 10:
                    print("Great session out there! I see you learned a few new tricks.")
                    pokemon_level = pokemon_level + 1
                    print("Hey, looks like you leveled up! Your current level is " + str(pokemon_level))
                    evolve()

                elif pokemon_level > 20:
                    print("You're a pro at this! I bet you will win your next battle.")
                    pokemon_level = pokemon_level + 1
                    print("Hey, looks like you leveled up! Your current level is " + str(pokemon_level))
                    evolve()
            if train == 2:
                if pokemon_level <= 10:
                    print("Great defending out there! I can see you are still learning.")
                    pokemon_level = pokemon_level + 1
                    print("Hey, looks like you leveled up! Your current level is " + str(pokemon_level))
                    evolve()

                elif pokemon_level <= 20 and pokemon_level > 10:
                    print("Great session out there! I see you learned a few new tricks.")
                    pokemon_level = pokemon_level + 1
                    print("Hey, looks like you leveled up! Your current level is " + str(pokemon_level))
                    evolve()

                elif pokemon_level > 20:
                    print("You're a pro at this! I bet you will win your next battle.")
                    pokemon_level = pokemon_level + 1
                    print("Hey, looks like you leveled up! Your current level is " + str(pokemon_level))
                    evolve()

        if activity == '2':
            outcome = random.randint(1,2) #50% chance to win or lose
            if outcome == 1:
                print("congrats you won your battle!")
                pokemon_level = pokemon_level + 1
                print("Hey, looks like you leveled up! Your current level is " + str(pokemon_level))
                evolve()
                battle_wins = battle_wins + 1

            if outcome == 2:
                print("Oh no it looks like you lost your battle!")
                battle_losses = battle_losses + 1

        if activity == '3':
            print("looks like you needed this rest!")
            print("your current level is " + str(pokemon_level))
            print("Name of your pokemon :" +(pokemon_name))
            print("Battle wins :"+ str(battle_wins))
            print("Battle losses :" + str(battle_losses))

        if activity == '4':
            break



#Main
game()
