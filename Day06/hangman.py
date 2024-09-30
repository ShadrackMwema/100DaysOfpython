import random
word_list =["apple","beekeeper","table","car"]
random_word = random.choice(word_list)
user_guess = input("Guess a letter: ")

for word in word_list:
    for letter in random.choice(word):
        if letter == user_guess:
            for letters in word:
                if letters == user_guess:
                    print(letters)
                else:
                    print("_")
                


