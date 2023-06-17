"""Given two integer arrays arr1 and arr2, return the minimum number of operations (possibly zero) needed to make arr1 strictly increasing.

In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].

If there is no way to make arr1 strictly increasing, return -1.

 

Example 1:

Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
Output: 1
Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].
Example 2:

Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
Output: 2
Explanation: Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6, 7].
Example 3:

Input: arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
Output: -1
Explanation: You can't make arr1 strictly increasing."""


from typing import List
import bisect


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:

        res = 0
        # sort the arr2
        arr2 = sorted(set(arr2))  # remove duplicates and sort

        # if arr1 is empty, return -1
        if len(arr1) == 0:
            return -1

        dp = {}

        def dfs(i, prev):
            if i >= len(arr1):
                return 0

            if (i, prev) in dp:
                return dp[(i, prev)]

            # find the index of the element just greater than prev
            idx = bisect.bisect_right(arr2, prev)
            # if arr1[i] is greater than prev, then we can replace
            # if idx is out of bound, then we can't replace
            replace = 1+dfs(i+1, arr2[idx]) if idx < len(arr2) else float('inf')

            # if arr1[i] is less than prev, then we have to replace it
            keep = dfs(
                i+1, arr1[i]) if arr1[i] > prev else float('inf')  # just

            dp[(i, prev)] = min(keep, replace)

            return dp[(i, prev)]

        res = dfs(0, -1)

        return res if res != float('inf') else -1


sol = Solution()


arr1 = [1, 5, 3, 6, 7]
arr2 = [1, 3, 2, 4]
print(sol.makeArrayIncreasing(arr1, arr2))
