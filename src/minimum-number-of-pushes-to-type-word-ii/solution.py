from collections import Counter


class Solution:
    # Define the method minimumPushes that takes a string 'word' as input and returns an integer.
    def minimumPushes(self, word: str) -> int:
        # Use Counter from the collections module to count the occurrences of each character in the input string.
        character_counts = Counter(word)
        # Get a list of the counts of each character, sorted in descending order.
        sorted_counts = sorted(character_counts.values(), reverse=True)

        # Initialize the total number of pushes required to 0.
        total_pushes = 0
        # Loop through the sorted counts with their indices.
        for index, count in enumerate(sorted_counts):
            # Calculate the multiplier based on the index. Every 8 characters increase the multiplier by 1.
            multiplier = index // 8 + 1
            # Add the product of the count and the multiplier to the total pushes.
            total_pushes += count * multiplier

        # Return the total number of pushes required.
        return total_pushes
