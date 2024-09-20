import random

test_seed =int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors."))
if test_seed == 0:
    your_choice = "ROCK"
elif test_seed == 1:
    your_choice = "PAPER"
else:
    your_choice = "SCISSORS"


choice = ['Rock', 'Paper', 'Scissors']
# answer = choice[random_num]
answer = random.choice(choice)
print(f"Computer chooses {answer}")
print(f"Your choice is {your_choice}")

if answer == 'Rock':
    if test_seed == 1:
        print("You win!")
    elif test_seed == 0:
        print("Draw!")
    else:
     print("You Lose!")
if answer == 'Paper':
    if test_seed == 1:
            print("Draw!")
    elif test_seed == 0:
        print("You lose!")
    else:
        print("You win!")

if answer == 'Scissors':
        if test_seed == 1:
            print("You lose!")
        if test_seed == 0:
            print("You win!")
        else:
            print("You Draw!")