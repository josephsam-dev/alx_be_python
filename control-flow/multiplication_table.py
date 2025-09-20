# Prompt the user to enter a number and convert it to an integer.
number = int(input("Enter a number to see its multiplication table: "))

# Use a for loop to iterate through numbers from 1 to 10.
# The range(1, 11) function generates numbers starting from 1 up to (but not including) 11.
for i in range(1, 11):
    # Calculate the product of the user's number and the current loop number (i).
    result = number * i

    # Print the result in the specified format using an f-string.
    print(f"{number} * {i} = {result}")
