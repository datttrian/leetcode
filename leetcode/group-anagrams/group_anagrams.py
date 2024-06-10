class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        def isAnagram(s: str, t: str) -> bool:
            if len(s) != len(t):
                return False

            for char in s:
                is_matched = False

                for i in range(len(t)):
                    if t[i] == char:
                        t = t[:i] + t[i + 1 :]
                        is_matched = True
                        break

                if not is_matched:
                    return False

            return True

        anagram_groups: list[list[str]] = []
        used = [False] * len(strs)

        for i in range(len(strs)):
            if not used[i]:
                group = [strs[i]]
                used[i] = True
                for j in range(i + 1, len(strs)):
                    if not used[j] and isAnagram(strs[i], strs[j]):
                        group.append(strs[j])
                        used[j] = True
                anagram_groups.append(group)

        return anagram_groups
