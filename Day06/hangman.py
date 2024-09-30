import random

# List of words
word_list = ["apple", "beekeeper", "table", "car"]

# Randomly choose a word from the word_list
computer_choice = random.choice(word_list)

# Create a list of underscores representing the word to guess
incomplete_word = ['_' for _ in computer_choice]

# Set number of attempts
attempts = len(computer_choice) + 3

# Start the game
while attempts > 0 and "_" in incomplete_word:
    print("Word to guess:", ' '.join(incomplete_word))  # Show current progress of the word
    user_guess = input("Guess a letter: ").lower()  # Get input from user

    if user_guess in computer_choice:
        # Replace underscores with the correct letter
        for index, letter in enumerate(computer_choice):
            if letter == user_guess:
                incomplete_word[index] = user_guess
    else:
        print(f"'{user_guess}' is not in the word.")

    attempts -= 1  # Decrease attempts
    print(f"Remaining attempts: {attempts}\n")

# End of game
if "_" not in incomplete_word:
    print(f"Congrats! You guessed the word '{computer_choice}'!")
else:
    print(f"Game Over! The word was '{computer_choice}'.")
