from collections import Counter

s = "abccccdd"

count = Counter(s)
print(count)
print(list((c // 2) * 2 for c in count.values()))

# length = sum()

print(list((c % 2 == 1 for c in count.values())))
