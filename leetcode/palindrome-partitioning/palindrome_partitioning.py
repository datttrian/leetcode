from typing import Tuple


def get_partitions(s: str) -> list[list[str]]:
    partitions: list[Tuple[list[str], int]] = [([s], 0)]
    result: list[list[str]] = []

    while partitions:
        partition, index = partitions.pop(0)

        if index == len(s):
            result.append(partition)
        else:
            for i in range(index + 1, len(s) + 1):
                new_partition = (
                    partition[:-1]
                    + [partition[-1][: i - index]]
                    + [partition[-1][i - index :]]
                )
                # Skip adding partition if it results in an empty string
                if new_partition[-1]:
                    partitions.append((new_partition, i))

    return result


def is_palindrome(sub: str) -> bool:
    return sub == sub[::-1]


s = "aab"
partitions = get_partitions(s)
print(partitions)
# result = [
#     partition
#     for partition in partitions
#     if all(is_palindrome(sub) for sub in partition)
# ]
# print(result)
