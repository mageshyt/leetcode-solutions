'''You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105'''


class Solution:
    def insert(self, intervals, newInterval):
        # edge case
        if len(intervals) == 0:
            return [newInterval]
        # find the place to insert the new interval so check interval end is > new interval start
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:

            i += 1

        # merge the intervals 
        # loop through the intervals and check if the new interval start is < interval end
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(
                newInterval[0], intervals[i][0])  # min of start
            newInterval[1] = max(newInterval[1], intervals[i][1])  # max of end
            intervals.pop(i)
            
        intervals.insert(i, newInterval)

        return intervals


if __name__ == "__main__":
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    print(Solution().insert(intervals, newInterval))
