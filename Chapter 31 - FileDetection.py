# Import OS MOD
import os 

# A path which is a file
path = "C:\\Users\\CSPC CCS\\test.txt"

# A path which is a directory
# Note directory is also know in common terms as "folder"
# path = "C:\\Users\\CSPC CCS"

#  IF the location exists, then proceed to this block
if os.path.exists(path):
    print("That location exists!")

    # Check if the path indicated is a file
    if os.path.isfile(path):
        print("That is a file")

    # Check if the path indicated is a directory
    elif os.path.isdir(path):
        print("That is a directory")

# ELSE, proceed to this block
else:
    print("That location does not exist!")