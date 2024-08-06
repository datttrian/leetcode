from collections import Counter

word = "aabbccddeeffgghhiiiiii"

counts = Counter(word)

queue = list(counts.values())
queue.sort(reverse=True)

print(queue)



push_count = 0

for key, value in enumerate(queue):
    push_count += value

    if key >= 8:
        push_count += value

print(push_count)
