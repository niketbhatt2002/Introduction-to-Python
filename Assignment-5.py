# Task 1 - Writing Functions
def greet_user(name):
    print(f"Hello, {name}! Welcome aboard.")

def add_numbers(a, b):
    return a + b

# Task 2 - Using Default Parameters
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

# Task 3 - Functions with Variable Arguments
def make_sandwich(*ingredients):
    print("Making a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

# Task 4 - Understanding Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Testing the functions
# Task 1
greet_user("Alice")
print(f"The sum of 5 and 10 is {add_numbers(5, 10)}.")

# Task 2
describe_pet("Buddy")
describe_pet("Whiskers", "cat")

# Task 3
make_sandwich("Lettuce", "Tomato", "Cheese")

# Task 4
print(f"Factorial of 5 is {factorial(5)}.")
print(f"The 6th Fibonacci number is {fibonacci(6)}.")
