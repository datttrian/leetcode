class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        def is_anagram(s: str, t: str) -> bool:
            if len(s) != len(t):
                return False

            for char in s:
                is_matched = False

                for i, c in enumerate(t):
                    if c == char:
                        t = t[:i] + t[i + 1 :]
                        is_matched = True
                        break

                if not is_matched:
                    return False

            return True

        anagram_groups: list[list[str]] = []
        used = [False] * len(strs)

        for i, str_i in enumerate(strs):
            if not used[i]:
                group = [str_i]
                used[i] = True
                for j, str_j in enumerate(strs[i + 1 :], start=i + 1):
                    if not used[j] and is_anagram(str_i, str_j):
                        group.append(str_j)
                        used[j] = True
                anagram_groups.append(group)

        return anagram_groups


solution = Solution()
print(solution.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
print(solution.groupAnagrams(strs=[""]))
print(solution.groupAnagrams(strs=["a"]))
