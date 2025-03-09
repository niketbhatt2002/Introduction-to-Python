import logging

# Set up logging to log errors into a file
logging.basicConfig(filename="error_log.txt", level=logging.ERROR)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Oops! Division by zero is not allowed.")
    return x / y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(" Invalid input! Please enter a valid number.")

def calculator():
    while True:
        print("\nWelcome to the Error-Free Calculator! ")
        print("1️ Addition")
        print("2️ Subtraction")
        print("3️ Multiplication")
        print("4️ Division")
        print("5️ Exit")

        choice = input("Choose an operation (1-5): ")

        if choice == '1':
            x = get_number("Enter the first number: ")
            y = get_number("Enter the second number: ")
            print(f"The result is: {add(x, y)}")

        elif choice == '2':
            x = get_number("Enter the first number: ")
            y = get_number("Enter the second number: ")
            print(f"The result is: {subtract(x, y)}")

        elif choice == '3':
            x = get_number("Enter the first number: ")
            y = get_number("Enter the second number: ")
            print(f"The result is: {multiply(x, y)}")

        elif choice == '4':
            try:
                x = get_number("Enter the first number: ")
                y = get_number("Enter the second number: ")
                result = divide(x, y)
                print(f"The result is: {result}")
            except ZeroDivisionError as e:
                print(f" {e}")
                logging.error(f"ZeroDivisionError occurred: {e}")
            except ValueError as e:
                print(f" {e}")
                logging.error(f"ValueError occurred: {e}")
            except Exception as e:
                print(f" Something went wrong: {e}")
                logging.error(f"Unexpected error occurred: {e}")

        elif choice == '5':
            print("Goodbye! ")
            break

        else:
            print(" Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    calculator()
