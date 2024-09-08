import random


test_seed = int(input("Enter a seed number: "))

random.seed(test_seed)

randomInt = random.randint(1,2)
print(randomInt)

if randomInt == 1:
    print("Head")
else:
    print("Tail")