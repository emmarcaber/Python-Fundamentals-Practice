# CHAPTER 55
# sort

# sort() = sort with lists
# sorted() = sort with iterables(tuples, dictionary, sets)

students = ["Embre", "ABEN", "Meracabe", "Hakdog"]

# PART 1 - Sorting with Lists

# sort the students list ascending
students.sort()
print(students)

print() # for space
# sort the students list descending
students.sort(reverse=True)
print(students)


# PART 2 - Sorting with Iterables

students_iterables = [
    ("Embre", "F", 75),
    ("ABEN", "A", 95),
    ("Meracabe", "B", 90),
    ("Hakdog", "C", 85),
]

print()
# Sort with Students Names
students_iterables.sort()
print(*students_iterables, sep="\n")

print()
# Sort with Remarks
# Key = get the grades for every tuple
#       then sort it
# Remember that sorted is an example of higher-order function
# With an argument of a function
sorted_with_remarks = sorted(students_iterables, key=lambda remarks: remarks[1])
print(*sorted_with_remarks, sep="\n")

print()
# Sort with Grades
sorted_with_grades = sorted(students_iterables, key=lambda grades: grades[2])
print(*sorted_with_grades, sep="\n")

print()
# Sort with Remarks but descending
sorted_with_remarks_descending = sorted(students_iterables, key=lambda remarks: remarks[1], reverse=True)
print(*sorted_with_remarks_descending, sep="\n")