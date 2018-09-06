text = input("Enter a string to count the words: ")
word_counts = {}
words = text.split()
for word in words:
    frequency = word_counts.get(word, 0)
    word_counts[word] = frequency + 1

longest_word_length = max(len(word) for word in words)

alphabetical_words = sorted(word_counts)
for word in alphabetical_words:
    print("{:{}} : {}".format(word, longest_word_length, word_counts[word]))
