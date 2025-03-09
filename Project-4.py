# Inventory Manager
inventory = {
    "apple": (10, 2.5),
    "banana": (20, 1.2)
}

def display_inventory():
    """Displays all items in the inventory."""
    print("\nCurrent Inventory:")
    for item, (quantity, price) in inventory.items():
        print(f"🛒 Item: {item}, Quantity: {quantity}, Price: ${price}")
    print(f"Total Inventory Value: ${calculate_total_value():.2f}")

def add_item():
    """Adds a new item to the inventory."""
    item = input("Enter item name: ").lower()
    if item in inventory:
        print("Item already exists! Use update option instead.")
        return
    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        inventory[item] = (quantity, price)
        print(f"{item} added successfully!")
    except ValueError:
        print("Invalid input. Please enter numeric values for quantity and price.")

def remove_item():
    """Removes an item from the inventory."""
    item = input("Enter item name to remove: ").lower()
    if item in inventory:
        del inventory[item]
        print(f" {item} removed successfully!")
    else:
        print("Item not found in inventory.")

def update_item():
    """Updates the quantity or price of an existing item."""
    item = input("Enter item name to update: ").lower()
    if item in inventory:
        try:
            quantity = int(input("Enter new quantity: "))
            price = float(input("Enter new price: "))
            inventory[item] = (quantity, price)
            print(f" {item} updated successfully!")
        except ValueError:
            print(" Invalid input. Please enter numeric values.")
    else:
        print(" Item not found in inventory.")

def calculate_total_value():
    """Calculates total value of the inventory."""
    return sum(quantity * price for quantity, price in inventory.values())

# Main loop
while True:
    print("\n Inventory Management System ")
    print("1️ Display Inventory")
    print("2️ Add Item")
    print("3️ Remove Item")
    print("4️ Update Item")
    print("5️ Exit")
    
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        display_inventory()
    elif choice == "2":
        add_item()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        update_item()
    elif choice == "5":
        print(" Exiting Inventory Manager. Have a great day!")
        break
    else:
        print(" Invalid choice! Please select a valid option.")
