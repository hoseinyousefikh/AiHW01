import random

number = random.randint(1, 100)

for i in range(5):
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == number:
        print("Great! Your guess is correct.")
        break
    elif guess < number:
        print("Guess higher.")
    else:
        print("Guess lower.")
else:
    print("Your chances are over.")
    print("The correct number was:", number)
