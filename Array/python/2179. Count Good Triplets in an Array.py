"""
You are given two 0-indexed arrays nums1 and nums2 of length n, both of which are permutations of [0, 1, ..., n - 1].

A good triplet is a set of 3 distinct values which are present in increasing order by position both in nums1 and nums2. In other words, if we consider pos1v as the index of the value v in nums1 and pos2v as the index of the value v in nums2, then a good triplet will be a set (x, y, z) where 0 <= x, y, z <= n - 1, such that pos1x < pos1y < pos1z and pos2x < pos2y < pos2z.

Return the total number of good triplets.

 

Example 1:

Input: nums1 = [2,0,1,3], nums2 = [0,1,2,3]
Output: 1
Explanation: 
There are 4 triplets (x,y,z) such that pos1x < pos1y < pos1z. They are (2,0,1), (2,0,3), (2,1,3), and (0,1,3). 
Out of those triplets, only the triplet (0,1,3) satisfies pos2x < pos2y < pos2z. Hence, there is only 1 good triplet.
Example 2:

Input: nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3]
Output: 4
Explanation: The 4 good triplets are (4,0,3), (4,0,2), (4,1,3), and (4,1,2).

"""

from typing import List
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)
        pos=[0]*n
        for idx,val in enumerate(nums2):
            pos[val]=idx

        mapped=[pos[val] for val in nums1]


        left=[0]*n
        bit=[0]*(n+2)

        # finwick tree

        def query(bit,idx):
            res=0
            while idx>0:
                res+=bit[idx]
                idx-=idx&(-idx)
            return res

        def update(bit,idx,val):
            while idx<=n:
                bit[idx]+=val
                idx+=idx&(-idx)

        for i in range(n):
            # how many elements are smaller than mapped[i]
            left[i]=query(bit,mapped[i])
            update(bit,mapped[i]+1,1)

        right=[0]*n
        bit=[0]*(n+2)

        for i in range(n-1,-1,-1):
            # how many elements are smaller than mapped[i]
            right[i]=query(bit,n) - query(bit,mapped[i]+1)
            update(bit,mapped[i]+1,1)

        return sum(left[i]*right[i] for i in range(n))

s=Solution()
print(s.goodTriplets([2,0,1,3],[0,1,2,3])) #1
