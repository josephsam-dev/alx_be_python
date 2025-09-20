# Prompt the user to enter the first number and convert it to a floating-point number.
num1 = float(input("Enter the first number: "))

# Prompt the user to enter the second number and convert it to a floating-point number.
num2 = float(input("Enter the second number: "))

# Prompt the user to choose an operation.
operation = input("Choose the operation (+, -, *, /): ")

# Use a match-case statement to perform the selected operation.
match operation:
    case '+':
        # Case for addition
        result = num1 + num2
        print(f"The result is {result}")
    case '-':
        # Case for subtraction
        result = num1 - num2
        print(f"The result is {result}")
    case '*':
        # Case for multiplication
        result = num1 * num2
        print(f"The result is {result}")
    case '/':
        # Case for division
        # First, check if the second number is zero to avoid an error.
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        # Default case for any other input
        print("Invalid operation selected.")
