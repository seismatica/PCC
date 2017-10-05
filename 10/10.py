# Find common words in a text-file book

filename = "pride.txt"
word = "the"

with open(filename) as file_object:
    content = file_object
    word_count = content.lower().count(word)
    print(word_count)