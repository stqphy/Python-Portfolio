#Pokemon Evolution Game
#Stephy

#Initialize
pokemon_level = 0
pokemon_name = "Pichu"
pokemon_name1 = "Pikachu"
pokemon_name2 = "Raichu"

import random

#Functions
def draw_ditto():
    print("""⠀⠀⠀⢠⡜⠛⠛⠿⣤⠀⠀⣤⡼⠿⠿⢧⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣀⡶⠎⠁⠀⠀⠀⠉⠶⠶⠉⠁⠀⠀⠈⠹⢆⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣀⡿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠶⠶⠶⠶⣆⡀⠀⠀⠀⠀
⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢣⡄⠀⠀⠀
⠛⣧⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀
⠀⠛⣧⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠀⠀⠀⠀⢠⡼⠃⠀⠀
⠀⠀⠿⢇⡀⠀⠀⠀⠀⠀⠀⠀⠰⠶⠶⢆⣀⣀⣀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀
⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀
⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀
⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢣⣤
⠀⣶⡏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿
⠀⠿⣇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⢀⣀⣸⠿
⠀⠀⠙⢳⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡞⠛⠛⠛⠛⠛⠛⣶⣶⣶⣶⡞⠛⠃⠀""")

def draw_pichu():
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⠟⢻⣿⣿⣿⣿
⣀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⠿⠋⠀⠀⠈⢡⣿⣿⡇
⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣄⠀⠀⠀⠀⠀⠀⠟⠁⠀⠀⠀⠀⠀⣼⣿⣿⠁
⠀⠹⣿⣿⣿⠿⡄⠉⠉⠙⠛⠻⢿⠀⠀⠀⣀⡀⠀⠘⠄⠀⠀⠀⠀⢠⣿⣿⡟⠀
⠀⠀⠙⣿⣿⣷⡀⠀⠀⠀⠀⠀⢸⠤⠂⠁⠀⠀⠀⠀⠀⠀⠀⠠⡀⠚⠛⠛⠀⠀
⠀⠀⠀⠈⢿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢤⣄⠀⠐⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠻⣿⣿⣿⠦⢲⠁⠀⢀⢀⠀⠀⠀⠀⠀⠸⣾⡿⢃⣠⡅⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⢸⠀⠐⣷⣾⡇⠀⠀⠂⠀⡀⠀⠀⣾⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣠⣤⣌⠉⠀⠀⠒⠒⠊⠀⠀⠀⢙⣟⠤⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣿⡇⠀⠀⠀⠀⠀⣀⣤⣶⠉⠀⠀⢠⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠔⠀⠀⠉⠉⡽⣿⣿⣿⢿⣿⠁⠀⢀⠔⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢤⢤⢴⠀⠋⠀⠁⠀⠉⠀⠸⣠⣴⣤⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠘⠀⢣⠀⠀⠀⠀⠀⠀⢀⠿⣿⣿⣿⣦⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢄⠀⢀⠀⠀⠀⠀⠀⢀⠈⠀⠈⠻⣿⠟⠋
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠁⠀⢠⠀⠀⠐⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⣀⣌⠇⠀⠀⠀⠀⠀""")

def draw_pikachu():
    print("""⠸⣷⣦⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⠀⠀⠀
⠀⠙⣿⡄⠈⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⠊⠉⣿⡿⠁⠀⠀⠀
⠀⠀⠈⠣⡀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠁⠀⠀⣰⠟⠀⠀⠀⣀⣀
⠀⠀⠀⠀⠈⠢⣄⠀⡈⠒⠊⠉⠁⠀⠈⠉⠑⠚⠀⠀⣀⠔⢊⣠⠤⠒⠊⠉⠀⡜
⠀⠀⠀⠀⠀⠀⠀⡽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠩⡔⠊⠁⠀⠀⠀⠀⠀⠀⠇
⠀⠀⠀⠀⠀⠀⠀⡇⢠⡤⢄⠀⠀⠀⠀⠀⡠⢤⣄⠀⡇⠀⠀⠀⠀⠀⠀⠀⢰⠀
⠀⠀⠀⠀⠀⠀⢀⠇⠹⠿⠟⠀⠀⠤⠀⠀⠻⠿⠟⠀⣇⠀⠀⡀⠠⠄⠒⠊⠁⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⡆⠀⠰⠤⠖⠦⠴⠀⢀⣶⣿⣿⠀⠙⢄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⣿⠃⠀⠀⠀⠀⠀⠀⠀⠈⠿⡿⠛⢄⠀⠀⠱⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠈⠓⠦⠀⣀⣀⣀⠀⡠⠴⠊⠹⡞⣁⠤⠒⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⠃⠀⠀⠀⠀⡌⠉⠉⡤⠀⠀⠀⠀⢻⠿⠆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠰⠁⡀⠀⠀⠀⠀⢸⠀⢰⠃⠀⠀⠀⢠⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢶⣗⠧⡀⢳⠀⠀⠀⠀⢸⣀⣸⠀⠀⠀⢀⡜⠀⣸⢤⣶⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠻⣿⣦⣈⣧⡀⠀⠀⢸⣿⣿⠀⠀⢀⣼⡀⣨⣿⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠻⠿⠿⠓⠄⠤⠘⠉⠙⠤⢀⠾⠿⣿⠟⠋ """)

def draw_raichu():
    print("""⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟫⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛🟫⬛⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬛⬜⬜⬜⬜
⬜⬜⬜⬛🟫🟫⬛⬜⬜⬜⬜⬛⬛🟫🟫🟫⬛⬜⬜⬛🟨⬛⬜⬜⬜
⬜⬜⬜⬛🟫⬛⬜⬜⬜⬜⬛🟫🟫🟨🟨⬛⬜⬜⬜⬛🟨⬛⬜⬜⬜
⬜⬜⬜⬛⬛⬛⬛⬛⬜⬛🟫🟫🟨🟨⬛⬜⬜⬜⬜⬛🟨🟨⬛⬜⬜
⬜⬜⬛⬛🟧🟧🟧🟧⬛🟫🟫🟨🟨⬛⬜⬜⬜⬜⬜⬛🟨🟨⬛⬜⬜
⬜⬛🟧🟧🟧🟧🟧🟧⬛🟫🟫🟨🟨🟨⬛⬛⬜⬜⬜⬛🟨🟨🟨⬛⬜
⬜⬛🟧🟧🟧🟧🟧🟧⬛⬛🟫🟫⬛⬛⬜⬛⬜⬛⬛⬛🟨🟨🟨⬛⬜
⬛🟧🟧🟧🟧🟧🟧🟧🟧⬛⬛⬛⬛⬜⬜⬜⬜⬛🟨⬛🟨🟨🟨🟨⬛
⬛🟧🟧🟧🟧🟧⬜⬛🟧🟧🟧🟧🟧⬛⬜⬜⬜⬜⬛🟨🟨⬛⬛🟨⬛
⬜⬛🟧🟧🟧🟧⬛⬛🟨🟨🟧🟧🟧⬛⬜⬜⬜⬜⬛🟨🟨⬛⬜⬛⬛
⬜⬜⬛🟧🟧🟧🟧🟧🟨🟨🟧🟧🟧🟧⬛⬜⬜⬜⬜⬛🟨⬛⬜⬜⬜
⬜⬛🟧⬛🟧🟧🟧🟧🟧⬛🟧🟧🟧🟫⬛⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜
⬜⬛🟧⬛⬜⬜🟧⬛⬛🟧🟧🟧🟧🟧🟧⬛⬜⬜⬜⬜⬜⬛⬜⬜⬜
⬜⬜⬛⬛⬛⬜⬛🟫🟧🟧🟧🟧🟧🟧🟫⬛⬜⬜⬜⬜⬜⬛⬛⬜⬜
⬜⬜⬜⬜⬛⬜⬛🟫🟫🟧⬛🟧🟧🟫🟫⬛⬜⬜⬜⬜⬜⬜⬛⬜⬜
⬜⬜⬜⬜⬛🟧⬜⬛⬛⬛🟧🟧🟧🟧🟧⬛⬛⬜⬜⬜⬜⬜⬛⬜⬜
⬜⬜⬜⬛🟫⬛⬛⬛⬜⬜🟧🟧🟧🟧⬛⬜⬛⬛⬜⬜⬜⬛⬛⬜⬜
⬜⬜⬜⬛⬛⬛⬛⬜⬛🟧🟧🟧🟧⬛⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟧🟧⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛🟫🟫🟫🟫⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜""")

def train():
    global pokemon_level
    pokemon_level = pokemon_level + 1
    print(pokemon_level)

def win():
    global pokemon_level
    pokemon_level = pokemon_level + 2

def lose():
    global pokemon_level
    pokemon_level = pokemon_level + 0

def evolve_pokemon():
    global pokemon_level

    if pokemon_level == 5:
        print("Your Pokemon's current level is: " + str(pokemon_level) + " " + "Congrats, your pokemon has evolved! " + "Your Pokemon has evolved to Pikachu!")

    if pokemon_level == 10:
        print("Your Pokemon's current level is: " + str(pokemon_level) + " " + "Congrats, your pokemon has evolved! " + "Your Pokemon has evolved to Raichu, it's final evolution!")

def evolve_pokemon1():
    global pokemon_level

    if pokemon_level == 5 or pokemon_level == 6:
        print("Your Pokemon's current level is: " + str(pokemon_level) + " " + "Congrats, your pokemon has evolved! " + "Your Pokemon has evolved to Pikachu!")

    if pokemon_level == 10 or pokemon_level == 11:
        print("Your Pokemon's current level is: " + str(pokemon_level) + " " + "Congrats, your pokemon has evolved! " + "Your Pokemon has evolved to Raichu, it's final evolution!")

def display_pokemon():
    if pokemon_level < 5:
        print("Current Pokemon: " + str(pokemon_name) + "   " + "Current level: " + str(pokemon_level))

    if pokemon_level >= 5 and pokemon_level <= 9:
        print("Current Pokemon: " + str(pokemon_name1) + "   " + "Current level: " + str(pokemon_level))

    if pokemon_level > 9:
        print("Current Pokemon: " + str(pokemon_name2) + "   " + "Current level: " + str(pokemon_level))

#Main
while True:
    print("Welcome to Pokemon Evolution Simulator")
    print("What would you like to do with your pokemon today?")
    print("""1.Train
2.Gym Battle
3.Rest (Display Info)
4.Exit""")
    option = int(input("(1-4) Option: "))

    if option == 1:
        train()
        evolve_pokemon()

    if option == 2:
        outcome = random.randint(1,2) #50% chance to win or lose
        if outcome == 1:
            print("Oh no, your Pokemon has lost its battle!")
            lose()
            print("Your Pokemon's current level is: " + str(pokemon_level))

        if outcome == 2:
            print("Yay, your Pokemon has won its battle!")
            win()
            print("Your Pokemon's current level is: " + str(pokemon_level))
            evolve_pokemon1()

    if option == 3:
        display_pokemon()

    if option == 4:
        break





