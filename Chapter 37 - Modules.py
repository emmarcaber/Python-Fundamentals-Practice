# module = a file containiong python code. May contain functions, classes, etc.
# Used with modular programming, which is to separate a program into parts

# First way
# import messages
# messages.hello()
# messages.bye()

# Second way
# import messages as msg
# msg.hello()
# msg.bye()

# Third way
from messages import hello, bye
hello()
bye()

# Fourth way
# from messages import *
# # this one is dangerous because you will import all functions
# # in the messages module
# hello()
# bye()


# help("modules") # show all the modules