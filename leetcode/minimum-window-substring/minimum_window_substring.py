class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''

        char_count: dict[str, int] = {}
        for char in t:
            char_count[char] = char_count.get(char, 0) + 1

        required_chars: int = len(char_count)
        formed_chars: int = 0
        left: int = 0
        right: int = 0
        min_len: float = float('inf')
        min_window: str = ''

        while right < len(s):
            char = s[right]
            char_count[char] = char_count.get(char, 0) - 1

            if char_count[char] == 0:
                formed_chars += 1

            while formed_chars == required_chars:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left : right + 1]

                char_left: str = s[left]
                char_count[char_left] += 1

                if char_count[char_left] > 0:
                    formed_chars -= 1

                left += 1

            right += 1

        return min_window
