def get_partitions(s: str) -> list[list[str]]:
    def backtrack(start: int, path: list[str]) -> None:
        if start == len(s):
            result.append(path)
            return
        for i in range(start, len(s)):
            backtrack(i + 1, path + [s[start : i + 1]])

    result: list[list[str]] = []
    backtrack(0, [])
    return result


s = "aab"
print(get_partitions(s))
