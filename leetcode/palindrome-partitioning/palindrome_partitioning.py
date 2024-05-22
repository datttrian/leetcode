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
                partitions.append((new_partition, i))

    return result


s = "aab"
print(get_partitions(s))
