"""Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""


class Solution:
    def merge(self, interval):
        # sort the intervals by stating point
        interval.sort(key=lambda x: x[0])
        # create a stack to hold the intervals
        stack = []
        # loop through the intervals
        for curr_interval in interval:
            if not stack:
                stack.append(curr_interval)

            else:
                start, end = curr_interval

                if start <= stack[-1][1]:
                    # now we have to merge the intervals by updating the end of the last interval

                    stack[-1][1] = max(end, stack[-1][1])

                else:
                    stack.append(curr_interval)

        return stack


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(Solution().merge(intervals))
