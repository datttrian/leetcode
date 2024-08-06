from collections import Counter

word = "aabbccddeeffgghhiiiiii"

print(Counter(word))

counts = Counter(word)

for key, value in counts:
    
