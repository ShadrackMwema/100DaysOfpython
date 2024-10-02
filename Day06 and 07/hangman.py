import random

# List of words
word_list = ["apple", "beekeeper", "table", "car"]

# Randomly choose a word from the word_list
computer_choice = random.choice(word_list)

# Create a list of underscores representing the word to guess
incomplete_word = ['_' for _ in computer_choice]

# Hangman stages (for incorrect guesses)
hangman_stages = [
    """
      ------
      |    |
           |
           |
           |
           |
    --------
    """,
    """
      ------
      |    |
      O    |
           |
           |
           |
    --------
    """,
    """
      ------
      |    |
      O    |
      |    |
           |
           |
    --------
    """,
    """
      ------
      |    |
      O    |
     /|    |
           |
           |
    --------
    """,
    """
      ------
      |    |
      O    |
     /|\\   |
           |
           |
    --------
    """,
    """
      ------
      |    |
      O    |
     /|\\   |
     /     |
           |
    --------
    """,
    """
      ------
      |    |
      O    |
     /|\\   |
     / \\   |
           |
    --------
    """
]

# Number of incorrect attempts before the hangman is fully drawn
max_attempts = len(hangman_stages) - 1
wrong_guesses = 0  # Track wrong guesses

# Start the game
while wrong_guesses < max_attempts and "_" in incomplete_word:
    # Show the current hangman state
    print(hangman_stages[wrong_guesses])

    # Show the current word with guessed letters and underscores
    print("Word to guess:", ' '.join(incomplete_word))

    # Ask the user for a letter
    user_guess = input("Guess a letter: ").lower()

    if user_guess in computer_choice:
        # Replace underscores with the correct letter
        for index, letter in enumerate(computer_choice):
            if letter == user_guess:
                incomplete_word[index] = user_guess
    else:
        # Increment the number of wrong guesses
        wrong_guesses += 1
        print(f"'{user_guess}' is not in the word.")

    print(f"Remaining attempts: {max_attempts - wrong_guesses}\n")

# End of the game
if "_" not in incomplete_word:
    print(f"Congrats! You guessed the word '{computer_choice}'!")
else:
    # Show the final hangman state
    print(hangman_stages[wrong_guesses])
    print(f"Game Over! The word was '{computer_choice}'.")
