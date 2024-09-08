import random
from itertools import count

test_seed = int(input("Enter a seed number: "))
random.seed(test_seed)

CSV_names = input("Enter every persons name separated by a comma: ")
names = CSV_names.split(",")

print(names)
names = len(names)

# begin=count(names[0])
print(names)
# last = len(names[-1])

print(begin,last)
# payer = random.choice(names)
payer = random.randint(begin,last)
print(payer)

