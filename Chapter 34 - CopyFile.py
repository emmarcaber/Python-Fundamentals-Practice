# CHAPTER 34

# copyfile() = copies contents of a file
# copy()     = copyfile() + permission mode + destination can be a directory
# copy2()    = copy() + copies metadata (file's creation and modification times)

# Module to copy files
import shutil

# Copy the contests of test.txt to copy.txt
shutil.copyfile('test.txt', 'copy.txt')

# shutil.copyfile(source, destination)
# NOTE: The destination can a path to a file