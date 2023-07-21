"""Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
"""
from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Check if the number of intervals is less than or equal to 1
        if len(intervals) <= 1:
            return 0

        # Sort the intervals based on their end times in ascending order
        intervals.sort(key=lambda interval: interval[1])
        print(intervals)
        # Initialize the end time of the first interval and the count of non-overlapping intervals
        end = intervals[0][1]
        count = len(intervals) - 1

        # Loop through the remaining intervals from the second one onwards
        for i in range(1, len(intervals)):
            # Get the start and end times of the current interval
            e2, s2 = intervals[i]

            # Check if the current interval overlaps with the previous selected interval
            if e2 >= end:
                # If not overlapping, update the end time to the current interval's end time
                end = e2
                # Decrease the count as we have found a non-overlapping interval
                count -= 1

        # Return the maximum number of non-overlapping intervals
        return count

intervals = [ [1,2],[2,3],[3,4],[1,3] ]

print(Solution().eraseOverlapIntervals(intervals))