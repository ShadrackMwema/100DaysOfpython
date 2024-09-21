import random

# Define the lists of characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '#', '$', '%', '^', '&', '*', '-']

# Take user input for the number of letters, numbers, and symbols
no_of_letters = int(input("Please enter the number of letters: "))
no_of_numbers = int(input("Please enter the number of numbers: "))
no_of_symbols = int(input("Please enter the number of symbols: "))

# Initialize an empty list for the password
password = []

# Add the random letters to the password list
for i in range(no_of_letters):
    password.append(random.choice(letters))

# Add the random numbers to the password list
for i in range(no_of_numbers):
    password.append(str(random.choice(numbers)))  # Convert numbers to string

# Add the random symbols to the password list
for i in range(no_of_symbols):
    password.append(random.choice(symbols))

# Print the password before shuffling (just for debug)
print(f"Password before shuffle: {password}")

# Shuffle the password list
random.shuffle(password)

# Print the password after shuffling (just for debug)
print(f"Password after shuffle: {password}")

# Join the shuffled list into a string to form the final password
final_password = ''.join(password)

# Print the final password
print(f"Your generated password is: {final_password}")
