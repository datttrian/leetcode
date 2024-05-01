class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)
        if index == -1:
            return word

        left, right = 0, index
        word_list = list(word)
        while left < right:
            word_list[left], word_list[right] = (
                word_list[right],
                word_list[left],
            )
            left += 1
            right -= 1

        return "".join(word_list)
