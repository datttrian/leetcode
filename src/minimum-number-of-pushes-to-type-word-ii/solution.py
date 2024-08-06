from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count the occurrences of each character in `word` using `Counter`
        character_counts = Counter(word)

        # Get the list of the counts sorted in descending order using `sorted`
        sorted_counts = sorted(character_counts.values(), reverse=True)

        # Loop through the sorted counts with their indices.
        total_pushes = 0
        for index, count in enumerate(sorted_counts):
            # Calculate the multiplier for every 8 characters based on the index. Every 8 characters increase the multiplier by 1.
            multiplier = index // 8 + 1
            # Add the product of the count and the multiplier to the total pushes.
            total_pushes += count * multiplier

        # Return the total number of pushes required.
        return total_pushes
