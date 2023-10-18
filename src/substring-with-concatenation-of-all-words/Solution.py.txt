from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        

        dict = Counter(words)
        res = []
        n = len(s)
        m = len(words[0])
        w = len(words)

        for k in range(m):
            seen = Counter()
            left = k
            currLen = 0
            for i in range(left, n - m + 1, m):
                temp = s[i : i + m]
                if temp not in dict:
                    seen.clear()
                    currLen = 0
                    left = i + m
                else:
                    seen[temp] += 1
                    currLen += 1
                    if seen[temp] > dict[temp]:
                        while seen[temp] > dict[temp]:
                            temp1 = s[left : left + m]
                            seen[temp1] -= 1
                            currLen -= 1
                            left += m
                if currLen == w:
                    res.append(left)
                    seen[s[left : left + m]] -= 1
                    currLen -= 1
                    left += m

        return res
