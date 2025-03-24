"""
You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).

Return the count of days when the employee is available for work but no meetings are scheduled.

Note: The meetings may overlap.

 

Example 1:

Input: days = 10, meetings = [[5,7],[1,3],[9,10]]

Output: 2

Explanation:

There is no meeting scheduled on the 4th and 8th days.

Example 2:

Input: days = 5, meetings = [[2,4],[1,3]]

Output: 1

Explanation:

There is no meeting scheduled on the 5th day.
"""
from typing import List
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # Time: O(n) | Space: O(1)
        count=0
        meetings.sort()
        start=1

        for meeting in meetings:
            count+=max(0,meeting[0]-start)
            start=max(start,meeting[1]+1)

        count+=max(0,days-start+1)

        return count

print(Solution().countDays(10,[[5,7],[1,3],[9,10]])) #2
print(Solution().countDays(5,[[2,4],[1,3]])) #1
