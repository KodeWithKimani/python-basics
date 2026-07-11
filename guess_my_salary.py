import random

print("Welcome to the salary guessing game.")

name = input("What's your name? ")
print("Hello,", name.title())

play = input("Would you like to play? (yes/no) ")

if play.lower() == "yes":

    print("Let's begin!")
    print("My salary is between 0 and 1000 dollars.")

    trials = int(input("How many attempts do you want? "))
    number = random.randint(0, 1000)

    while trials > 0:

        print("Attempts left:", trials)

        guess = int(input("Make your guess: "))

        if guess == number:
            print("🎉 Correct! You guessed my salary!")
            break

        elif guess < number:
            difference = number - guess

            if difference <= 20:
                print("Very close! Go just a little higher.")
            elif difference <= 100:
                print("Close! Go higher.")
            else:
                print("Way too low! Go much higher.")

        else:
            difference = guess - number

            if difference <= 20:
                print("Very close! Go just a little lower.")
            elif difference <= 100:
                print("Close! Go lower.")
            else:
                print("Way too high! Go much lower.")

        trials -= 1

    if trials == 0 and guess != number:
        print("Out of attempts! My salary was $.",number)

else:
    print("Hmm, okay then. We'll play next time.")