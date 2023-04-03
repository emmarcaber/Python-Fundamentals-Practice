# CHAPTER 64
# threading     = a flow of execution. Like a separate order of instructions.
#                However, each thread takes a turn running to achieve concurrency
#                GIL = (global interpreter lock),
#                allows only one thread to hold the control of the Python Interpreter at any one time

# Program/Tasks have two (2) categories:
# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing

# i/o bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#             use multithreading

import threading
import time

def eat_breakfast():
    time.sleep(3) # seconds
    print("You eat breakfast")

def drink_coffee():
    time.sleep(4) # seconds
    print("You drink coffee")

def study():
    time.sleep(5) # seconds
    print("You finished studying")


# Creates a thread for eat_breakfast
# name_of_thread.start()
eat_breakfast_thread = threading.Thread(target=eat_breakfast, args=()) 
eat_breakfast_thread.start()

drink_coffee_thread = threading.Thread(target=drink_coffee, args=()) 
drink_coffee_thread.start()

study_thread = threading.Thread(target=study, args=()) 
study_thread.start()

# THREAD SYNCHRONIZATION
# the main thread waits for all of the threads 
# to finish, only thereafter the main thread will execute
# eat_breakfast_thread.join()
# drink_coffee_thread.join()
# study_thread.join()

# eat_breakfast()
# drink_coffee()
# study()

# this are executed first since the main thread
# has its own separate order of instructions
# and the main thread is not already in charge of the other threads
print(threading.active_count())
print(threading.enumerate())
print(time.process_time())  # amount of seconds take with main thread to finish