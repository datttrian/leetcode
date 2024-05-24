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
