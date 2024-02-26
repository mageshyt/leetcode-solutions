"""
You are given a 0-indexed integer array nums, and you are allowed to traverse between its indices. You can traverse between index i and index j, i != j, if and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest common divisor.

Your task is to determine if for every pair of indices i and j in nums, where i < j, there exists a sequence of traversals that can take us from i to j.

Return true if it is possible to traverse between all such pairs of indices, or false otherwise.



Example 1:

Input: nums = [2,3,6]
Output: true
Explanation: In this example, there are 3 possible pairs of indices: (0, 1), (0, 2), and (1, 2).
To go from index 0 to index 1, we can use the sequence of traversals 0 -> 2 -> 1, where we move from index 0 to index 2 because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1, and then move from index 2 to index 1 because gcd(nums[2], nums[1]) = gcd(6, 3) = 3 > 1.
To go from index 0 to index 2, we can just go directly because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1. Likewise, to go from index 1 to index 2, we can just go directly because gcd(nums[1], nums[2]) = gcd(3, 6) = 3 > 1.
Example 2:

Input: nums = [3,9,5]
Output: false
Explanation: No sequence of traversals can take us from index 0 to index 2 in this example. So, we return false.
Example 3:

Input: nums = [4,3,12,8]
Output: true
Explanation: There are 6 possible pairs of indices to traverse between: (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), and (2, 3). A valid sequence of traversals exists for each pair, so we return true.
"""

from typing import List
class UF:
    def __init__(self):
        self.UF = {}

    def find(self, x):
        self.UF.setdefault(x, x)
        if x != self.UF[x]:
            self.UF[x] = self.find(self.UF[x])
        return self.UF[x]

    def union(self, x, y):
        self.UF[self.find(x)] = self.find(y)

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf=UF()
        factor_idx={} # f -> idx of value with factor f

        for idx, num in enumerate(nums):
            f=2 # start from 2 because 0 and 1 are already connected
            while f*f<=num:
                # if its the factor
                if num % f == 0:
                    # if already in the factor_idx then connect them
                    if f in factor_idx:
                        uf.union(idx,factor_idx[f])
                    # else add it to the factor_idx
                    else:
                        factor_idx[f]=idx

                    while num % f == 0:
                        num//=f
                f+=1
            if num> 1:
                if num in factor_idx:
                    uf.union(idx,factor_idx[num])
                else:
                    factor_idx[num]=idx

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if not uf.connected(i,j):
                    return False

        return True


if __name__ == '__main__':
    nums = [4,3,12,8]
    s=Solution()
    print(s.canTraverseAllPairs(nums))
