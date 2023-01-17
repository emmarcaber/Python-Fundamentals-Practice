# Import the Random module
import random

x = random.randint(1, 6) 		# generate a random number from 1 to 6
y = random.random()			# generate a random floating number between 0 and 1

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList) 	# generate a random choice from the list

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

random.shuffle(cards)		    # shuffle the cards randomly

print(x)
print(y)
print(z)
print(cards)
