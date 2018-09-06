text = "this is very nice and is good"
word_counts = {}
words = text.split()
for word in words:
    frequency = word_counts.get(word, 0)
    word_counts[word] = frequency + 1

print(word_counts)