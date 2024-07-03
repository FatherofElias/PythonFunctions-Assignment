# Question 2  The Shopping List Maker
# Task 1 Write a function that lets the user add items to a list

# solution

# Function to add items to a shopping list
def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f"'{item}' has been added to your shopping list.")

# Task 2 

# solution 

# Function to remove items from a shopping list
def remove_item(shopping_list, item):
    try:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from your shopping list.")
    except ValueError:
        print(f"'{item}' is not in the shopping list.")

# Task 3

# solution

# Function to print the entire shopping list in a formatted way
def print_list(shopping_list):
    if shopping_list:
        print("Your shopping list:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
    else:
        print("Your shopping list is empty.")

# Main function to run the shopping list program
def shopping_list_program():
    shopping_list = []
    while True:
        print("\nOptions:")
        print("1. Add item")
        print("2. Remove item")
        print("3. View shopping list")
        print("4. Quit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            item = input("Enter the item to add: ")
            add_item(shopping_list, item)
        elif choice == '2':
            item = input("Enter the item to remove: ")
            remove_item(shopping_list, item)
        elif choice == '3':
            print_list(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the shopping list program
shopping_list_program()