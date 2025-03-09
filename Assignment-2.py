import time  # Importing time module for countdown delay

# Task 1 - Counting Down with Loops
starting_number = int(input("Enter the starting number for countdown: "))

while starting_number > 0:
    print(starting_number, end=" ", flush=True)  # Print countdown numbers in a single line
    time.sleep(1)  # Adding a 1-second delay for a real countdown effect
    starting_number -= 1

print("Reverse Number Printed Successful! ")  # Message after countdown ends

# Task 2 - Multiplication Table with for Loops
num = int(input("\nEnter a number to generate its multiplication table: "))

print(f"\nMultiplication Table for {num}:")
for i in range(1, 11):  # Loop from 1 to 10
    print(f"{num} x {i} = {num * i}")

# Task 3 - Find the Factorial
fact_num = int(input("\nEnter a number to find its factorial: "))
factorial = 1  # Initializing factorial value

for i in range(1, fact_num + 1):
    factorial *= i  # Multiply each number from 1 to the given number

print(f"The factorial of {fact_num} is {factorial}.")  # Printing the final result
