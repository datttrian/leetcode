class Solution:
    def maxArea(self, height: list[int]) -> int:
        left_pointer, right_pointer = 0, len(height) - 1
        max_water = 0

        while left_pointer < right_pointer:
            current_water = (right_pointer - left_pointer) * min(
                height[left_pointer], height[right_pointer]
            )
            max_water = max(max_water, current_water)

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_water
