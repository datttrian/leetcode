# Zigzag Conversion


The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given
number of rows like this: (you may want to display this pattern in a
fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R
        

And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a
number of rows:

    string convert(string s, int numRows);
        

 

**Example 1:**

    Input: s = "PAYPALISHIRING", numRows = 3
        Output: "PAHNAPLSIIGYIR"
        

**Example 2:**

    Input: s = "PAYPALISHIRING", numRows = 4
        Output: "PINALSIGYAHRPI"
        Explanation:
        P     I    N
        A   L S  I G
        Y A   H R
        P     I
        

**Example 3:**

    Input: s = "A", numRows = 1
        Output: "A"
        

 

**Constraints:**

- `1 <= s.length <= 1000`
- `s` consists of English letters (lower-case and upper-case), `','` and
  `'.'`.
- `1 <= numRows <= 1000`


# Intuition
The problem is to convert a string into a specific zigzag pattern with a given number of rows and then read it line by line. This zigzag pattern simulates writing the string in a sawtooth shape, and the function reads it by concatenating the characters line by line.

# Approach
1. Handle the edge case: If the number of rows is 1 or greater than or equal to the length of the string, return the original string since the zigzag pattern is not applicable.
2. Initialize a list of strings (`rows`) to represent each row of the zigzag pattern. The list has a length equal to the number of rows.
3. Initialize variables: `current_row` to keep track of the current row, and `going_down` as a flag indicating whether the movement is down or up in the zigzag.
4. Iterate over each character in the string:
   - Append the character to the string corresponding to the current row in the `rows` list.
   - If the current row is at the top or bottom of the zigzag, reverse the direction by toggling the `going_down` flag.
   - Move to the next row in the zigzag pattern based on the direction.
5. Concatenate all rows in the `rows` list to form the final zigzag pattern string.

# Complexity
- Time complexity: O(n), where n is the length of the input string, as the function iterates over all characters once.
- Space complexity: O(n), where n is the length of the input string, due to the space required to store the zigzag pattern across `numRows`, which collectively will not exceed the length of the input string.

# Code
```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        current_row = 0
        going_down = False

        for char in s:
            rows[current_row] += char
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1

        return ''.join(rows)
```