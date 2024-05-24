# Given scores
score = [
    1,
    0,
    9,
    5,
    0,
    0,
    3,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    2,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]

# Generate dictionary mapping each letter to its score
score_dict = {chr(97 + i): score[i] for i in range(len(score))}

# Print the dictionary
print(score_dict)

# Given list of letters
letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]

# Create dictionary to count occurrences of each letter
letter_counts: dict[str, int] = {}
for letter in letters:
    if letter in letter_counts:
        letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1


# Print the dictionary
print(letter_counts)

# Given list of words
words = ["dog", "cat", "dad", "good"]

print(words)
