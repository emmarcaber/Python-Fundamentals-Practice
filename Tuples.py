# tuple =   collection which is ordered and unchangeable
#           used to group together related data

student = ("Bro", 21, "Male")

print(student.count("Bro")) # counts the total number of elements "Bro" in tuple student
print(student.index("Male")) # finds the index that matches the tuple student

# prints all elements in the student
for x in student:
    print(x)

# checks if "Bro" in the tuple student
if "Bro" in student:
    print("Bro is here!")