from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: defaultdict[str, List[str]] = defaultdict(list)

        for word in strs:
            # Sort the characters of the word to create a unique key for
            # anagrams
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word].append(word)

        return list(anagrams.values())
