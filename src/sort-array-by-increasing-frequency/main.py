class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums_count = Counter(nums)
        group_count = {}

        for num, count in nums_count.items():
            if count in group_count:
                group_count[count].append(num)
            else:
                group_count[count] = [num]
        
        for group, count in group_count.items():
            count.sort(reverse=True)

        result = []
        
        for count, nums in sorted(group_count.items()):
            for num in nums:
                for _ in range(count):
                    result.append(num)
        
        return result
