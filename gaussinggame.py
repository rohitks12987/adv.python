#GuessingTheNumber Game And caluclate the number of attempts and output the result to the user.
import random
number_to_guess = random.randint(1, 100)
attempts = 0
guessed_correctly = False
print("Welcome to the Guessing Game! I'm thinking of a number between 1 and 100.")
while not guessed_correctly:
    try:
        user_guess = int(input("Enter your guess: "))
        attempts += 1
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100.")