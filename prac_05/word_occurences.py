
"""
Word Occurrences
Estimate: 30 minutes
Actual: 60 minutes
"""

text = input("Text: ")
words = text.split()
word_counts = {}

# Count word occurrences
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

# Find the longest word for alignment
max_length = max(len(word) for word in word_counts)

# Display word counts in sorted order with alignment
for word in sorted(word_counts):
    print(f"{word:{max_length}} : {word_counts[word]}")
