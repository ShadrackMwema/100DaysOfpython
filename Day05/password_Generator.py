import random

# Define the lists of characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '#', '$', '%', '^', '&', '*', '-']

# Take user input for the number of letters, numbers, and symbols
no_of_letters = int(input("Please enter the number of letters: "))
no_of_numbers = int(input("Please enter the number of numbers: "))
no_of_symbols = int(input("Please enter the number of symbols: "))

# Generate random letters, numbers, and symbols
chosen_letters = [random.choice(letters) for _ in range(no_of_letters)]
chosen_numbers = [str(random.choice(numbers)) for _ in range(no_of_numbers)]
chosen_symbols = [random.choice(symbols) for _ in range(no_of_symbols)]

# Combine all the characters
password_list = chosen_letters + chosen_numbers + chosen_symbols

# Shuffle the password to make it more random
random.shuffle(password_list)

# Join the list into a final password string
final_password = ''.join(password_list)

# Print the final password
print(f"Your generated password is: {final_password}")
