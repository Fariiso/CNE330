import random
def findNumber():
    # generates a random number between 1-100
    correct_number=random.randint(1, 100)
    # Explain the rules of the game.
    print("""Hi lets play "Guess A Number Game!"
        You can guess any number between 1 and 100.
        If you guess correctly, you win!
        You will have unlimited chances.
        To end the game, type EXIT!""")

    usernumber =""

    #This code will repeat a task until the user guesses the correct number or exits the game.
    while (usernumber!=correct_number  ):
        usernumber=input("What is the number: ")
            #if user enter "EXIT", exit the loop.
        if (usernumber=="EXIT"):
            print("Game Over!")

            break
            #If the user guesses a larger number, display a message and repeat.
        if int(usernumber) > correct_number:
            print("The number is too high, please try again!")
            #if the number is too low, the question repeats.
        elif int(usernumber) < correct_number:
            print("The number is too low, please try again!")
        else:

            print("Congradulations. You Win!")


findNumber()


