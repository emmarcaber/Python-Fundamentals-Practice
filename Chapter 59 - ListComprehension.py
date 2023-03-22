# CHAPTER 59
# List Comprehension = a way to create a new list with less syntax
#                      can mimic certain lambda functions, easier to read
#                      list = [expression for item in iterable]
#                      list = [expression for item in iterable if conditional]
#                      list = [expression if/else for item in iterable]


# PART 1 - DEMONSTRATING LIST COMPREHENSION
#          WITH FOR LOOP to create a new list

# Looping method
squares = []                    # create an empty list
for i in range(1, 11):          # create a for loop
    squares.append(i * i)       # define what each loop iteration should do
print(squares)

# Now, with list comprehension
squares = [i * i for i in range(1, 11)]
print(squares)



# PART 2 - COMBINATION OF LIST COMPREHENSION WItH CONDITIONS

# list to filter with conditions
students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

# With list and filter
passed_students = list(filter(lambda x : x >= 60, students))
print(passed_students)

# Result is Like the method above, but with list comprehension
passed_students = [i for i in students if i >= 60]
print(passed_students)

# IF i is greater than or equal to 60, append the grade as a number
# ELSE append "FAILED" in the passed_students list
passed_students = [i if i >= 60 else "FAILED" for i in students]
print(passed_students)