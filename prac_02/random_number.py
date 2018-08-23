import random
print(random.randint(5,20))
# This generates an integer between and including 5 and 20
# Largest number could be 20; Smallest number could be 5

print(random.randrange(3, 10, 2))
# Number between 3 and 10 in steps of two
# Could not produce a 4 as it is in steps of 2, meaning only odd numbers could be generated (3,5,7,9)
# Therefore, smallest number 3, largest number 9

print(random.uniform(2.5,5.5))
# float between 2.5 and 5.5
# smallest number 2.5, largest 5.5
