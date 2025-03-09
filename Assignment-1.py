# Task 1 - Variables: Your First Python Intro
name = "Niket Bhatt"  # Replace with your name or any fictional name
age = 22  # Replace with your age
height = 5.4  # Replace with your height in feet

# Printing the friendly introduction message
print(f"Hey there, my name is {name}! I’m {age} years old and {height} feet tall.")

# Task 2 - Operators: Playing with Numbers
num1 = 10  # You can choose any number
num2 = 3   # Another number of your choice

# Performing mathematical operations
print("\nLet's do some math with", num1, "and", num2, "!")

print("The sum of", num1, "and", num2, "is", num1 + num2)  # Addition
print("The difference when subtracting", num2, "from", num1, "is", num1 - num2)  # Subtraction
print("The product of", num1, "and", num2, "is", num1 * num2)  # Multiplication
print("The result of dividing", num1, "by", num2, "is", num1 / num2)  # Division

# Task 3 - Conditional Statements: The Number Checker
user_input = float(input("\nEnter a number to check if it's positive, negative, or zero: "))

if user_input > 0:
    print("This number is positive. Awesome!")
elif user_input < 0:
    print("This number is negative. Better luck next time!")
else:
    print("Zero it is. A perfect balance!")
