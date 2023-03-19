# CHAPTER 13
# nested loops =		The "inner loop" will finish all of it's iterations before
#						finishing one iteration of the "outer loop"

rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
symbol = input("Enter a symbol to use: ")

# outer loop is for rows,
# whereas inner loop is for columns
for i in range(rows):
	for j in range(columns):
		print(symbol, end="")
	print()

# another common example for nested loops,
# is to display some asterisks like this:
#
# 	*
# 	* *
# 	* * *
# 	* * * *
# 	* * * * *
#
# You can solve this using the code below:
# for i in range(6):
#	for j in range(i):
#		print("*", end="")
#	print()