import string

filename = input("Enter the filename: ")
with open(filename, "r") as f:
    contents = f.read()
    contents = contents.translate(str.maketrans("", "", string.punctuation))
    words = contents.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    sorted_word_counts = sorted(word_counts.items())
    for word, count in sorted_word_counts:
        print(f"{word}: {count}")
print("done with task")
