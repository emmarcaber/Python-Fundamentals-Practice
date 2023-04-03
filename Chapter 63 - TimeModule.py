# CHAPTER 63
# time module

import time

print(time.ctime(0))            # convert a time expressed in seconds since epoch to a readable string
                                # epoch = when your computer thinks time began (reference point) 
                                # NOTE: epoch depends on your operating system

print(time.time())              # return current seconds since epoch

print(time.ctime(time.time()))  # current date and time

time_object = time.localtime()  # creates a time_object which is the current local time
time_object = time.gmtime()
print(time_object)

# PART 1
# Date to String
# time.strftime() converts a time object to string
# time.strftime(format:string, time_object_to_convert_to_string: time)
# NOTE: you can view the documentation in: docs.python.org/3/library/time.html
time_string = time.strftime("%B %d %Y %I:%M:%S", time_object)
print(time_string)



# PART 2
# String to Date
# time.strptime() will parse a string representation
# of a time and date and return a time object
# time.strptime(string_in_time_format: string, format: string)

time_string = "20 April, 2020"
time_object = time.strptime(time_string, "%d %B, %Y")
print(time_object)


# time.asctime() accepts a time tuple
# and converts it to a date and time object
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)

# converts time tuple to time object since epoch
string_seconds = time.mktime(time_tuple)
print(string_seconds)