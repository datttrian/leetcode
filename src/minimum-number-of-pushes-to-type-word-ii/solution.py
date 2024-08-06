from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:

        # Count the occurrences of each character in `word` using `Counter`
        character_counts = Counter(word)

        # Get the list of the counts sorted in descending order using `sorted`
        sorted_counts = sorted(character_counts.values(), reverse=True)

        # Initialize the total pushes required
        total_pushes = 0

        # Loop through the sorted counts with their indices
        for index, count in enumerate(sorted_counts):

            # Calculate the multiplier for every 8 characters based on the index
            multiplier = index // 8 + 1

            # Add to the total pushes the product of the count and the multiplier
            total_pushes += count * multiplier

        # Return the total number of pushes required.
        return total_pushes
