text = "Yoooooooooooooooo\nThis is some text\nHave a good one!\n"

# The 'w' is parameter to indicate the file will be written
with open('test.txt', 'w') as file:
    file.write(text) # Write the value of text to the test.txt file