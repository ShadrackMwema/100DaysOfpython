import random
from itertools import count

test_seed = int(input("Enter a seed number: "))
random.seed(test_seed)

CSV_names = input("Enter every persons name separated by a comma: ")
names = CSV_names.split(",")

print(names)
x =(len(names)-1)
random_num = random.randint(0, x)

print(names)


payer = names[random_num]

print(payer)

