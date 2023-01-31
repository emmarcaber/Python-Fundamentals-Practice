
try:
    # Opens a file
    # NOTE: With open() automatically closes the file
    with open('test.txt') as file:
        print(file.read()) # Prints the contents of the file

    # Checks if the file is closed
    print(file.closed)

# Catches the exception that occurs when
# the file was not found
except FileNotFoundError:
    print("That file was not found :(")

# NOTE: Always use try-except block when opening a file