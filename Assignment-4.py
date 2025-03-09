# Task 1 - Working with Lists
favorite_fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Appending a new fruit
favorite_fruits.append('fig')

# Removing a fruit
favorite_fruits.remove('apple')

# Reversed list using slicing
reversed_fruits = favorite_fruits[::-1]

# Printing results
print("Original list:", ['apple', 'banana', 'cherry', 'date', 'elderberry'])
print("After adding a fruit:", favorite_fruits)
print("After removing a fruit:", favorite_fruits)
print("Reversed list:", reversed_fruits)

# Task 2 - Exploring Dictionaries
personal_info = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Adding a new key-value pair
personal_info["favorite color"] = "Blue"

# Updating the city
personal_info["city"] = "Los Angeles"

# Printing keys and values
print("\nDictionary Keys:", ", ".join(personal_info.keys()))
print("Dictionary Values:", ", ".join(str(value) for value in personal_info.values()))

# Task 3 - Using Tuples
favorite_things = ("Inception", "Bohemian Rhapsody", "1984")

# Attempting to change a tuple element (will throw an error)
try:
    favorite_things[0] = "Interstellar"
except TypeError:
    print("\nOops! Tuples cannot be changed.")

# Printing length of the tuple
print("Favorite things:", favorite_things)
print("Length of tuple:", len(favorite_things))
