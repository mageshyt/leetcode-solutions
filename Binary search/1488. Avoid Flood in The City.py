"""
our country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the nth lake, the nth lake becomes full of water. If it rains over a lake that is full of water, there will be a flood. Your goal is to avoid floods in any lake.

Given an integer array rains where:

rains[i] > 0 means there will be rains over the rains[i] lake.
rains[i] == 0 means there are no rains this day and you can choose one lake this day and dry it.
Return an array ans where:

ans.length == rains.length
ans[i] == -1 if rains[i] > 0.
ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.
If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.

Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes.

 

Example 1:

Input: rains = [1,2,3,4]
Output: [-1,-1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day full lakes are [1,2,3]
After the fourth day full lakes are [1,2,3,4]
There's no day to dry any lake and there is no flood in any lake.
Example 2:

Input: rains = [1,2,0,0,2,1]
Output: [-1,-1,2,1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day, we dry lake 2. Full lakes are [1]
After the fourth day, we dry lake 1. There is no full lakes.
After the fifth day, full lakes are [2].
After the sixth day, full lakes are [1,2].
It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another acceptable scenario.
"""
n
from typing import List
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        res = [-1] * len(rains)

        full_lakes = {} # lake -> day it got full
        dry_days = [] # days we can dry a lake

        for day, lake in enumerate(rains):
            if lake > 0:
                if lake in full_lakes:
                    # Need to dry this lake before today
                    last_full_day = full_lakes[lake]
                    idx = self.upper_bound(dry_days, last_full_day)
                    if idx == len(dry_days):
                        return []
                    dry_day = dry_days[idx]
                    res[dry_day] = lake
                    dry_days.pop(idx)
                full_lakes[lake] = day
            else:
                dry_days.append(day)
                res[day] = 1

        return res


    def upper_bound(self,arr,target):
        low,high = 0,len(arr)-1
        while low <= high:
            mid = (low+high)//2
            if arr[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        return low
solution = Solution()
print(solution.avoidFlood([1,2,3,4]))
print(solution.avoidFlood([1,2,0,0,2,1]))
