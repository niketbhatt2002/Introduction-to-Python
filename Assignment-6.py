# Task 1 - Understanding Python Exceptions
def divide_by_user_input():
    try:
        num = int(input("Enter a number: "))
        result = 100 / num
        print(f"100 divided by {num} is {result}")
    except ZeroDivisionError:
        print("Oops! You cannot divide by zero.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Task 2 - Types of Exceptions
def generate_exceptions():
    # IndexError
    try:
        my_list = [1, 2, 3]
        print(my_list[5])  # Accessing an out-of-range index
    except IndexError:
        print("IndexError occurred! List index out of range.")

    # KeyError
    try:
        my_dict = {"name": "Alice", "age": 25}
        print(my_dict["city"])  # Accessing a non-existent key
    except KeyError:
        print("KeyError occurred! Key not found in the dictionary.")

    # TypeError
    try:
        result = "Hello" + 5  # Attempting to add a string and an integer
    except TypeError:
        print("TypeError occurred! Unsupported operand types.")

# Task 3 - Using try...except...else...finally
def safe_division():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ZeroDivisionError:
        print("Oops! You cannot divide by zero.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    else:
        print(f"The result is {result}.")
    finally:
        print("This block always executes.")

# Running the functions
print("\n--- Task 1 ---")
divide_by_user_input()

print("\n--- Task 2 ---")
generate_exceptions()

print("\n--- Task 3 ---")
safe_division()
