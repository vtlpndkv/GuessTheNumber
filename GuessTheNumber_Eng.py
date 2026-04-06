print("GuessTheNumber")
print("__________")
print("Hello! A number from 1 to 100 has been chosen, guess it")
print("You have 5 attempts")
print("Will you be able to guess at least once?")
print("__________")

import random
number = random.randint(1, 100)
attempts = 5
again = "yes"

while again == "yes":
    if attempts != 0:
        number_input = int(input("Enter a number from 1 to 100: "))
        if number_input > 0 and number_input <= 100:
            attempts -= 1
            if number_input > number:
                if attempts != 0:
                    print("❌ Wrong! The hidden number is SMALLER")
                    print("-1 attempt, remaining:", attempts)
                    print("__________")
            elif number_input < number:
                if attempts != 0:
                    print("❌ Wrong! The hidden number is BIGGER")
                    print("-1 attempt, remaining:", attempts)
                    print("__________")
            else:
                print("🥳 Hurray!")
                print("✅ You guessed the hidden number!")
                print("__________")
                print("Do you want to play again?")
                print("yes/no")
                again = input().lower()
                print("__________")
                if again == "yes":
                    attempts = 5
                    number = random.randint(1, 100)
                    print("New game")
                elif again != "yes":
                    print("Game over!")
        else:
            print("❌ The number must be between 1 and 100!")
            print("__________")
    else:
        if number_input != number:
            print("__________")
            print("😥 You lost!")
            print("The hidden number was:", number)
            print("__________")
            print("Do you want to play again?")
            print("yes/no")
            again = input().lower()
            print("__________")
        if again == "yes":
            attempts = 5
            number = random.randint(1, 100)
            print("New game")
        elif again != "yes":
            print("Game over!")