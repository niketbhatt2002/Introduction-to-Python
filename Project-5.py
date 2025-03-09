import turtle

def factorial(n):
    """Recursive function to calculate factorial"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Recursive function to calculate Fibonacci number"""
    if n <= 0:
        return "Invalid input! Enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def draw_fractal(length, depth):
    """Recursive function to draw a fractal tree using turtle"""
    if depth == 0:
        return
    turtle.forward(length)
    turtle.left(30)
    draw_fractal(length * 0.7, depth - 1)
    turtle.right(60)
    draw_fractal(length * 0.7, depth - 1)
    turtle.left(30)
    turtle.backward(length)

def fractal_tree():
    """Sets up turtle for drawing a fractal tree"""
    turtle.speed(0)
    turtle.left(90)
    turtle.up()
    turtle.backward(100)
    turtle.down()
    draw_fractal(100, 5)
    turtle.done()

while True:
    print("\n Recursive Functions Menu ")
    print("1️ Calculate Factorial")
    print("2️ Find Fibonacci Number")
    print("3️ Draw a Recursive Fractal")
    print("4️ Exit")
    
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        try:
            num = int(input("Enter a number to find its factorial: "))
            if num < 0:
                print("Please enter a non-negative integer.")
            else:
                print(f"The factorial of {num} is {factorial(num)}.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    elif choice == "2":
        try:
            num = int(input("Enter the position of the Fibonacci number: "))
            if num < 1:
                print(" Please enter a positive integer.")
            else:
                print(f"The {num}th Fibonacci number is {fibonacci(num)}.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    elif choice == "3":
        print(" Drawing Fractal Tree... (Close the window to return)")
        fractal_tree()

    elif choice == "4":
        print(" Exiting the program. Have a great day!")
        break

    else:
        print("Invalid choice! Please select a valid option.")
