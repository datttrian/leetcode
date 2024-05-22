def get_all_substrings(s: str) -> list[str]:
    substrings: list[str] = []
    length = len(s)
    for i in range(length):
        for j in range(i + 1, length + 1):
            substrings.append(s[i:j])
    return substrings


def is_palindrome(sub: str) -> bool:
    return sub == sub[::-1]


def main(s: str) -> list[str]:
    substrings = get_all_substrings(s)
    result: list[str] = []
    for substring in substrings:
        if is_palindrome(substring):
            result.append(substring)
    return result


# Example usage:
input_string = "abba"
print(main(input_string))
