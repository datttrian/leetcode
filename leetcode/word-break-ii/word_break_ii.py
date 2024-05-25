class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        def helper(start: int) -> list[str]:
            if start in memo:
                return memo[start]

            res: list[str] = []
            if start == len(s):
                res.append("")

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordDict:
                    sub_sentences = helper(end)
                    for sub in sub_sentences:
                        if sub:
                            res.append(word + " " + sub)
                        else:
                            res.append(word)

            memo[start] = res
            return res

        wordDict = list(wordDict)
        memo: dict[int, list[str]] = {}
        return helper(0)
