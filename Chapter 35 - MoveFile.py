# CHAPTER 35

import os

source = "test.txt"
destination = "C:\\Users\\CSPC CCS\\test.txt"

try:
    
    # Check if the path exists
    if os.path.exists(destination):
        print("There is already a file there")
    
    # Else, if there is no path existing
    # Move the file to the destination
    else:
        os.replace(source, destination)
        print(source + " was moved")

# If there is no file to move
# catch the exception
except FileNotFoundError:
    print(source + " was not found")