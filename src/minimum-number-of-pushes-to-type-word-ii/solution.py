from collections import Counter

word = "aabbccddeeffgghhiiiiii"

counts = Counter(word)

queue = list(counts.values())
queue.sort(reverse=True)

print(queue)



push_count = 0
index 
