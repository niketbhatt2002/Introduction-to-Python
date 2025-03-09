# Task 1 - String Slicing and Indexing
my_string = "Python is amazing!"

# Extracting parts of the string
first_word = my_string[:6]  # Extract "Python"
amazing_part = my_string[11:-1]  # Extract "amazing"
reversed_string = my_string[::-1]  # Reverse the string

# Printing results
print("First word:", first_word)
print("Amazing part:", amazing_part)
print("Reversed string:", reversed_string)

# Task 2 - String Methods
string_value = " hello, python world! "

# Using different string methods
stripped_value = string_value.strip()  # Remove extra spaces
capitalized_value = stripped_value.capitalize()  # Capitalize first letter
replaced_value = stripped_value.replace("world", "universe")  # Replace word
uppercase_value = stripped_value.upper()  # Convert to uppercase

# Printing results
print("\nOriginal String:", string_value)
print("After strip():", stripped_value)
print("After capitalize():", capitalized_value)
print("After replace():", replaced_value)
print("After upper():", uppercase_value)

# Task 3 - Check for Palindromes
user_input = input("\nEnter a word to check if it's a palindrome: ").lower()  # Convert input to lowercase
reversed_input = user_input[::-1]  # Reverse the string

# Checking if the word is a palindrome
if user_input == reversed_input:
    print(f"Yes, '{user_input}' is a palindrome!")
else:
    print(f"No, '{user_input}' is not a palindrome.")
