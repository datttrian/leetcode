class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        def backtrack(start: int, path: list[str]):
            if start == len(s) and len(path) == 4:
                result.append('.'.join(path))
                return

            for end in range(start + 1, min(start + 4, len(s) + 1)):
                segment = s[start:end]
                if 0 <= int(segment) <= 255 and (
                    len(segment) == 1 or segment[0] != '0'
                ):
                    backtrack(end, path + [segment])

        result: list[str] = []
        backtrack(0, [])
        return result
