# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y

# Function to display menu and get user's choice
def display_menu():
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")
    return choice

# Main function to operate the calculator
def main():
    print("Welcome to Simple Calculator!")
    
    while True:
        choice = display_menu()

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            else:
                print("Invalid input. Please enter a valid number (1/2/3/4/5).")
        
        except ValueError:
            print("Invalid input. Please enter numeric values for numbers.")

if __name__ == "__main__":
    main()
