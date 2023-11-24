from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        max_reach = nums[0]
        steps = nums[0]
        jumps = 1

        for i in range(1, n):
            if i == n - 1:
                return jumps

            max_reach = max(max_reach, i + nums[i])
            steps -= 1

            if steps == 0:
                jumps += 1
                if i >= max_reach:
                    return -1

                steps = max_reach - i

        return -1
