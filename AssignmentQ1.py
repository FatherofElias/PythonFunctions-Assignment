#Question 1 


#Task 1 Create functions for each arithmetic operation.


# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract one number from another
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide one number by another
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

#Task 2 Use inputs to ask the user what operation they want to perform, 
# and what numbers they want to use.


# Main function to perform the calculator operations
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The result is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The result is: {divide(num1, num2)}")
    else:
        print("Invalid input")

calculator()


#Task 3  Ensure your code can handle division by zero and other potential 
# errors. So if you divide by 0,
#  there is error handling set up to prevent an error from 
# showing in the console.


# updated code with try and except 
# valueError function to account for division by zero or any other error.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error! Division by zero."

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"The result is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result is: {divide(num1, num2)}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")
    else:
        print("Invalid input! Please select a valid operation.")

calculator()
