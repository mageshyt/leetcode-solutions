"""
You are given an integer n which represents an array nums containing the numbers from 1 to n in order. Additionally, you are given a 2D array conflictingPairs, where conflictingPairs[i] = [a, b] indicates that a and b form a conflicting pair.

Remove exactly one element from conflictingPairs. Afterward, count the number of non-empty subarrays of nums which do not contain both a and b for any remaining conflicting pair [a, b].

Return the maximum number of subarrays possible after removing exactly one conflicting pair.


"""

from typing import List
class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        right = [[] for _ in range(n + 1)]
        for a, b in conflictingPairs:
            right[max(a, b)].append(min(a, b))

        ans = 0
        left = [0, 0]
        bonus = [0] * (n + 1)
        for r in range(1, n + 1):
            for l in right[r]:
                if l > left[0]:
                    left[1] = left[0]
                    left[0] = l
                elif l > left[1]:
                    left[1] = l

            ans += r - left[0]

            if left[0] > 0:
                bonus[left[0]] += left[0] - left[1]

        return ans + max(bonus)

print(Solution().maxSubarrays(5, [[1, 2], [2, 3], [3, 4]]))  # 9

