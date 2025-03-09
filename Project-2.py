import random

# Step 1: Generate a random number
number_to_guess = random.randint(1, 100)
attempts = 0
max_attempts = 10  # Bonus: Limit attempts

print(" Welcome to the Number Guessing Game!")
print("Guess the number (between 1 and 100). You have 10 attempts.\n")

# Step 2: Loop for user guesses
while attempts < max_attempts:
    try:
        user_guess = int(input(f"Attempt {attempts+1}/{max_attempts}: Enter your guess: "))
        attempts += 1

        # Step 3: Check guess
        if user_guess < 1 or user_guess > 100:
            print(" Please guess a number between 1 and 100.")
        elif user_guess < number_to_guess:
            print(" Too low! Try again.\n")
        elif user_guess > number_to_guess:
            print("Too high! Try again.\n")
        else:
            print(f" Congratulations! You guessed the number {number_to_guess} in {attempts} attempts! ")
            break  # Exit the loop when guessed correctly

    except ValueError:
        print(" Invalid input! Please enter a valid number.\n")

# Step 4: If user exceeds max attempts
if attempts == max_attempts:
    print(f"Game over! The correct number was {number_to_guess}. Better luck next time!")
