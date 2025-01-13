#Multiplication Quiz
#Stephy

#Init
import random

#Functions

def multiplication_quiz():
    print("Welcome to Multiplication Quiz!")
    question = 0 #counter for number of questions
    right = 0 #counter for questions that are right
    wrong = 0 #counter for questions that are wrong

    while True: #while loop
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        product = num1 * num2

        answer = int(input("What is the product of " + str(num1) + " and " + str(num2) + "? ")) #Player inputs a integer as their answer for the question

        if answer == product:
            print("You're correct!")
            question = question + 1
            right = right + 1
            print("Question " + str(question) + " is done!")

        else:
            print("You're wrong!")
            question = question + 1
            wrong = wrong + 1
            print("Question " + str(question) + " is done!")

        if question == 5: #ends loop after 5 questions
            break

    print("Your total score is: " + str(right) + " right and " + str(wrong) + " wrong! Thank you for participating!") #Prints out how many questions you got right and how many you got wrong

#Main
multiplication_quiz()





