# for i in range(1, 21, 2):
#     print(i, end=' ')
# print()
#
# for i in range(0, 101, 10):
#     print(i, end=' ')
# print()
#
# for i in range(20, 0, -1):
#     print(i, end=' ')
# print()

# stars_number=int(input("How many stars?: "))
# for i in range(0, stars_number, 1):
#     print("*", end=' ')

lines_number = int(input("How many lines of increasing stars?: "))
for i in range(0, lines_number+1, 1):
    for j in range(0, i, 1):
        print("*", end="")
    print()

