class Solution(object):
    def maxArea(self, height):
        max_area = 0
        l = 0
        r = len(height) - 1
        while l < r:
            area = (r - l) * min(height[r], height[l])
            max_area = max(max_area, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
