class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return []


solution = Solution()
print(solution.twoSum(numbers=[2, 7, 11, 15], target=9))
print(solution.twoSum(numbers=[2, 3, 4], target=6))
print(solution.twoSum(numbers=[-1, 0], target=-1))
