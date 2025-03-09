# Voter Eligibility Checker 

# Step 1: Ask for the user's age
try:
    age = int(input("How old are you? "))

    # Step 2: Validate the input
    if age < 0:
        print("Age cannot be negative! Please enter a valid age.")
    elif age >= 18:
        print("Congratulations! You are eligible to vote. Go make a difference! ")
    else:
        years_left = 18 - age
        print(f"Oops! You're not eligible yet. But hey, only {years_left} more years to go! ")

except ValueError:
    print("Invalid input! Please enter a valid number.")

# Step 3: Test with different ages and ensure it handles errors gracefully
