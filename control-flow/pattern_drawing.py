# Prompt the user to enter the size of the pattern and convert it to an integer.
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the rows. This will be used by the while loop.
row = 0

# The 'while' loop will handle each row of the pattern.
# It continues as long as the row counter is less than the desired size.
while row < size:
    # The nested 'for' loop will handle the columns for the current row.
    # It will print one asterisk for each column.
    for column in range(size):
        # The 'end=""' argument tells the print function to not add a newline character.
        # This keeps all the asterisks for a single row on the same line.
        print("*", end="")

    # After the inner 'for' loop finishes printing all asterisks for a row,
    # this 'print()' statement adds a newline character to move to the next line.
    print()

    # Increment the row counter to move on to the next row in the next iteration.
    row += 1
