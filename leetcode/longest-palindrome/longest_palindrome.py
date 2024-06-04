from collections import Counter

s = "abccccdd"

count = Counter(s)

length = sum((c // 2) * 2 for c in count.values())

print(list((c % 2 == 1 for c in count.values())))
