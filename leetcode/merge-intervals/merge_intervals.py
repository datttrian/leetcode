from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merge overlapping intervals and return non-overlapping intervals.

        Parameters:
        - intervals (List[List[int]]): The input array of intervals.

        Returns:
        - List[List[int]]: Non-overlapping intervals.
        """
        if not intervals:
            return []

        intervals.sort(
            key=lambda x: x[0],
        )  # Sort intervals based on the start time

        merged_intervals = [intervals[0]]

        for interval in intervals[1:]:
            if interval[0] <= merged_intervals[-1][1]:  # Overlapping intervals
                merged_intervals[-1][1] = max(
                    merged_intervals[-1][1],
                    interval[1],
                )
            else:
                merged_intervals.append(interval)

        return merged_intervals
