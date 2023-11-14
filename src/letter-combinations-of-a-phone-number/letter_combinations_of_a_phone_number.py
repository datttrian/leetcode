from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Generate all possible letter combinations for a given string of digits.

        Summary:
        Given a string of digits, this method produces all possible
        combinations of letters that can be formed by mapping each digit to
        its respective set of letters on a phone keypad.

        Description:
        This method iterates through each digit in the input string, using a
        mapping of digits to letters on a phone keypad. For each digit, it
        generates new combinations by appending each letter to the existing
        combinations. The final result is a list of all possible letter
        combinations.

        Algorithm Parameters:
        - digits (str): The input string consisting of digits for which letter
                       combinations need to be generated.

        Returns:
        List[str]: A list of strings representing all possible letter
        combinations.

        Raises:
        - None

        Complexity:
        - Time: O(4^n), where n is the length of the input digits string. In
        the worst case, each digit can contribute up to 4 letters (7 and 9
        have 4 letters each). The method iterates through each digit,
        resulting in an exponential time complexity.
        - Space: O(4^n), as the space complexity is also exponential due to
        the number of combinations generated.
        """
        if not digits:
            return []

        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        # Initialize the combinations list with an empty string as a starting
        # point
        combinations = ['']

        # Iterate through each digit in the input
        for digit in digits:
            # Create a new list to store combinations for the current digit
            new_combinations: List[str] = []

            # Iterate through existing combinations
            for combination in combinations:
                # Append each letter corresponding to the current digit to the
                # existing combinations
                for letter in phone_map[digit]:
                    new_combinations.append(combination + letter)

            # Update the combinations list with the newly generated
            # combinations for the current digit
            combinations = new_combinations

        # Return the final list of combinations
        return combinations
