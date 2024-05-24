from itertools import combinations


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
score_dict: dict[str, int] = {chr(97 + i): score[i] for i in range(len(score))}


# list of words
words = ["dog", "cat", "dad", "good"]


# Function to generate all subsets
def generate_subsets(words: list[str]) -> list[list[str]]:
    subsets: list[list[str]] = []
    for i in range(len(words) + 1):
        for combo in combinations(words, i):
            subsets.append(list(combo))
    return subsets


# Function to calculate the score of a word
def calculate_word_score(word: str, score_dict: dict[str, int]) -> int:
    return sum(score_dict[char] for char in word)


# Function to check if a subset of words can be formed with the available letters
def can_form_words(words: list[str], letter_counts: dict[str, int]) -> bool:
    temp_letter_counts = letter_counts.copy()
    for word in words:
        for char in word:
            if temp_letter_counts.get(char, 0) == 0:
                return False
            temp_letter_counts[char] -= 1
    return True


# Generate all subsets
all_subsets: list[list[str]] = generate_subsets(words)

# Initialize max score
max_score = 0

# Calculate the maximum score for any valid subset
for subset in all_subsets:
    if can_form_words(subset, letter_counts):
        subset_score = sum(
            calculate_word_score(word, score_dict) for word in subset
        )
        max_score = max(max_score, subset_score)

# Print the maximum score
print(max_score)
