#MadLibs
#Stephy

#Functions
def madlibs():
    #Introduction
    print("Welcome to MadLibs! Please enter words for the given prompt so we can create a story for you!")
    print("Please provide a word or phrase for the following: ")
    #Collecting input from the user
    number = (input("Number: "))
    place = (input("Place: "))
    adj1 = (input("Adjective: "))
    adj2 = (input("Adjective: "))
    gd = (input("Good Deed: (if using a verb, don't use a verb that ends with ing)"))
    present1 = (input("Present: "))
    present2 = (input("Present: "))
    food1 = (input("Food: "))
    drink = (input("Drink: "))
    noun1 = (input("Noun: "))
    food2 = (input("Food: "))
    animal = (input("Animal: "))
    verb = (input("Verb: (don't use a verb that ends with ing)"))
    noun2 = (input("Noun: "))
    adj3 = (input("Adjective: "))
    name = (input("Name: "))
    noun3 = (input("Noun: "))
    #prints the story out with the words the user inputs
    print(" ")
    print("Dear Santa, ")
    print(" ")
    print("This Christmas, I am " + str(number) + " years old. " + "I live in " + str(place) + " and it is " + str(adj1) + " here. " + "I have been very " + str(adj2) + " this year and try to always " + str(gd) + ".")
    print("I would like " + str(present1) + " and " + str(present2) + " for Christmas please. " + "I promise to leave you " + str(food1) + " and " + str(drink) + " on the " + str(noun1) + " on Christmas Eve and " + str(food2) + " for your " + str(animal) + ".")
    print("And don't forget to " + str(verb) + " under the " + str(noun2) + "!")
    print("I hope you have a very " + str(adj3) + " holiday season!")
    print(" ")
    print("                 Love your friend, ")
    print("                 " + str(name))
    print(" ")
    print("PS: Say hi to " + str(noun3) + " for me!")


#Main
madlibs()

