class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict: dict[int, int] = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_dict:
                return [num_dict[complement], i]

            num_dict[num] = i

        return []


if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6

    # Place a breakpoint at the line of function call
    # For example:
    # breakpoint()  # Before calling the function
    result = Solution().twoSum(nums, target)

    print("Indices:", result)
