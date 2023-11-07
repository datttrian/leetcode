`lengthOfLongestSubstring` calculates the length of the longest substring without repeating characters in a given string `s`. It uses the sliding window approach, where a window is a range of characters that does not contain any duplicates. Here's how it works, step by step, with the example string `s = "abcabcbb"`:

1. **Initialization**:
   - A dictionary `char_index_map` is created to keep track of the most recent index where each character occurs.
   - Two pointers `left` and `right` are initialized to represent the boundaries of the sliding window. `left` is the start index, and `right` is the end index of the sliding window.
   - `max_length` is initialized to 0 to keep track of the length of the longest substring found.

2. **First Iteration (`right` = 0, `char` = 'a')**:
   - The character 'a' is not in `char_index_map`, so the current window is from index 0 to index 0.
   - `char_index_map` is updated with `char_index_map['a'] = 0`.
   - `max_length` is updated to `max(0, 0 - 0 + 1)` which is 1.

3. **Second Iteration (`right` = 1, `char` = 'b')**:
   - The character 'b' is not in `char_index_map`, so the current window is from index 0 to index 1.
   - `char_index_map` is updated with `char_index_map['b'] = 1`.
   - `max_length` is updated to `max(1, 1 - 0 + 1)` which is 2.

4. **Third Iteration (`right` = 2, `char` = 'c')**:
   - The character 'c' is not in `char_index_map`, so the current window is from index 0 to index 2.
   - `char_index_map` is updated with `char_index_map['c'] = 2`.
   - `max_length` is updated to `max(2, 2 - 0 + 1)` which is 3.

5. **Fourth Iteration (`right` = 3, `char` = 'a')**:
   - The character 'a' is in `char_index_map` at index 0. Since 0 is not greater than or equal to the current `left` (0), the `left` is not updated.
   - `char_index_map` is updated with `char_index_map['a'] = 3`.
   - `max_length` remains 3, as `max(3, 3 - 0 + 1)` is 4, but the window actually moved to start after the last 'a'.

Now the window is from index 1 to index 3.

6. **Continuing the process**, the algorithm will update the `left` boundary whenever it encounters a repeated character that lies within the current window. Each time it moves `left`, it effectively removes the previous occurrence of the character from the current window.

7. **Final Iteration (`right` = 7, `char` = 'b')**:
   - At the last character 'b', `char_index_map` contains `{'a': 6, 'b': 5, 'c': 4}`.
   - The character 'b' was last seen at index 5, so `left` is updated to 5 + 1 = 6.
   - `char_index_map` is updated with `char_index_map['b'] = 7`.
   - `max_length` is updated to `max(3, 7 - 6 + 1)` which is 3.

At the end of the loop, the algorithm returns the `max_length`, which is the length of the longest substring without repeating characters. For the string "abcabcbb", the longest substring without repeating characters is "abc", and its length is 3.