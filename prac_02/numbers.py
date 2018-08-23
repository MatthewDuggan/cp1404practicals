INPUT_FILE = "numbers.txt"
input_file = open(INPUT_FILE,'r')
total = 0
for line in input_file:
    number = int(line)
    total += number
print(total)
input_file.close()