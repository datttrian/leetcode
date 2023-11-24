from typing import List


class Solution:
    def insert(
        self,
        intervals: List[List[int]],
        newInterval: List[int],
    ) -> List[List[int]]:
        """
        Insert a new interval into a list of non-overlapping intervals.

        Parameters:
        - intervals (List[List[int]]): The input array of non-overlapping
        intervals.
        - new_interval (List[int]): The interval to be inserted.

        Returns:
        - List[List[int]]: Intervals after the insertion.
        """
        result: List[List[int]] = []
        i = 0
        n = len(intervals)

        # Add intervals that come before the new interval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        result.append(newInterval)

        # Add intervals that come after the new interval
        while i < n:
            result.append(intervals[i])
            i += 1

        return result
