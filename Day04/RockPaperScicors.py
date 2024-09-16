import random

test_seed =int(input("Type 0 for Rock, 1 for Paper, 2 for Scissors."))

random.seed(test_seed)
random_num = random.randint(1,3)

choice = ['Rock', 'Paper', 'Scissors']
answer = choice[random_num]
print(answer)

if answer == 'Rock':
    if random_num == 1: