# CHAPTER 65
# daemon thread = a thread that runs in the background, not important for program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be killed, stay alive until task is complete

#                 ex. background tasks, garbage collection, waiting for input, long running process

import threading 
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print(f"Logged in for {count} seconds")

# this thread is hard to kill
# you must just close or stop the application
# x = threading.Thread(target=timer)

# makes the thread a daemon thread
# if the main thread is done, stop this daemon thread already
x = threading.Thread(target=timer, daemon=True)
x.start()

# x.setDaemon(True)     # sets a thread a daemon or not
print(x.daemon)         # checks if a thread is a daemon or not

answer = input("Do you wish to exit?")