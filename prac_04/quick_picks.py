import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45

number_of_quick_picks = int(input("How many quick picks would you like?: "))

quick_pick = []
for picks in range(0, number_of_quick_picks):
    for lines in range(0, NUMBERS_PER_LINE):
        new_number = random.randint(MINIMUM,MAXIMUM)
        while new_number in quick_pick:
            new_number = random.randint(MINIMUM, MAXIMUM)
        quick_pick.append(new_number)
        quick_pick.sort()
    print(quick_pick)








