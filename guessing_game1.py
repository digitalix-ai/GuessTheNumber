import sys
from random import choice

first = int(sys.argv[1])
last = int(sys.argv[2])

random_num = choice(range(first, last+1))
match = 0

while not match:
	try:
		guess = int(input(f'Guess the number I have in mind between {first} and {last}: '))
		while first <= guess <= last:
			if guess < random_num:
				guess = int(input('Try a bigger number: '))
			elif guess > random_num:
				guess = int(input('Try a smaller number: '))
			else:
				print("Correct! You're a genius!")
				match = 1
				break
		else:
			print('Please choose a number in the specified range')
			
	except ValueError:
		print('Please enter a number')
