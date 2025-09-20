# pattern_drawing.py

# Ask the user for the size of the pattern
try:
    size = int(input("Enter the size of the pattern: "))
    if size <= 0:
        print("Please enter a positive integer.")
        exit()
except ValueError:
    print("Invalid input! Enter a positive integer.")
    exit()

# Initialize row counter
row = 0

# Outer while loop to iterate through rows
while row < size:
    # Inner for loop to print asterisks in one row
    for col in range(size):
        print("*", end="")  # Print '*' without newline
    print()  # Move to next line after finishing a row
    row += 1  # Increment row counter

