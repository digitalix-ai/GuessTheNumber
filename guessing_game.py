import sys
from random import choice

first = int(sys.argv[1])
last = int(sys.argv[2])

random_num = choice(range(first, last+1))

guess = int(input('guess the number I have in mind between your specified numbers: '))

correct = False

while not correct:
	if guess < random_num:
		guess = int(input('try a bigger number: '))
	elif guess > random_num:
		guess = int(input('try a smaller number: '))
	else:
		print("Correct! You're a genius!")
		correct = True

