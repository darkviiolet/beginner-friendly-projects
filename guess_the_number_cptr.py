import random


def guess(x):
    # define the variable random number to store the generated number
    random_number = random.randint(1, x)
    # initiate guess to zero

    guess = 0

    # while loop to ask the user again about his guess until he get it right
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        # if statements to help the user guess
        if guess < random_number:
            print("sorry, guess again. Too low.")
        elif guess > random_number:
            print("sorry, guess again. Too high.")
    print(f"yaay! you guessed the number {random_number} correctly!!")


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "C":
        guess = random.randint(low, high)
        feedback = input(f"is {guess} too high (H), too low (L), or correct (C)\n")
        if feedback == "H":
            high = guess - 1
        elif feedback == "L":
            low = guess + 1
    print(f"Yay! the computer guessed your number correctly! ")
# calling the function with 50 as a parameter
# guess(50)
# calling the second function with 10 as a parameter


computer_guess(10)
