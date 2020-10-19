# GuessTheNumber
Number guessing game in Python, using the modules "sys" and "random"

************************************************************************************************************************
guessing_game.py

The game can be run in a command line, using 'python guessing_game.py', followed by a smaller and a larger number.
Example: python guessing game.py 5 15

After pressing 'enter' the user will be prompted to guess the number the computer has in mind between the specified
number. The user will be prompted to choose smalller or bigger numbers, untill they guess the correct one.

************************************************************************************************************************

guessing_game1.py

Improved version of the game, with added error handling. The game starts in the same way as in the first file. But 
then prompts the user to choose a number in the specified range between the first and second numbers (arguments) 
entered at the start of the program. Then if the user try guessing a number outside of that range, another prompt 
reminds about the condition. If characters other than integers are being entered, there is different prompt showing,
reminding that the guess must be a number. 
