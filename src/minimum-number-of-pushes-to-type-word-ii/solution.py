from collections import Counter

word = "aabbccddeeffgghhiiiiii"

counts = Counter(word)

queue = list(counts.values())

print(queue)
