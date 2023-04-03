# CHAPTER 60
# zip(*iterables) = aggregates elements from two or more iterables (list, tuples, sets, etc.)
#                   creates zip object with paired elements stored in tuples for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")

# Zips the usernames and passwords, then convert it to a dictionary
users = dict(zip(usernames, passwords))

# Check what data type user variable is
print(type(users))
print(users)

for (key, value) in users.items():
    print(f"{key} {value}")


# Actually you can also just do it like this
# You don't need to create a dictionary
# Just a loop
print(*zip(usernames, passwords))
for (username, password) in zip(usernames, passwords):
    print(f"{username} {password}")
