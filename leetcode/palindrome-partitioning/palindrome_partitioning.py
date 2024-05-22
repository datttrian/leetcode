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

                new_partition = [part for part in new_partition if part]
                partitions.append((new_partition, i))

    return result


def is_palindrome(sub: str) -> bool:
    return sub == sub[::-1]


s = "aab"
partitions = get_partitions(s)
result = [
    partition
    for partition in partitions
    if all(is_palindrome(sub) for sub in partition)
]
print(result)
