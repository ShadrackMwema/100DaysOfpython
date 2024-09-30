import random
word_list =["apple","beekeeper","table","car"]
random_word = random.choice(word_list)
user_guess = input("Guess a letter: ")

choice_list = []
for word in word_list:
    for letter in user_guess:
        for i in range(len(word)):
            if letter == word[i]:
                choice_list.append(word)

print(choice_list)
computer_choice = random.choice(choice_list)
print(computer_choice)

incomplete_word = []
print(len(computer_choice))


i = 0
while i < len(computer_choice):

    if computer_choice[i] == user_guess:

        incomplete_word.append(computer_choice[i])
    else:

        incomplete_word.append("_")
    print("Hello")

    i+=1
print(incomplete_word)
final =''.join(incomplete_word)
print(final)

