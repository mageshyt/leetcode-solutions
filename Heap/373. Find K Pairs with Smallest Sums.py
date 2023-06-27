from typing import List
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res=[]
        if not nums1 or not nums2:
            return res
        
        queue=[]
        def push(i,j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue,(nums1[i]+nums2[j],i,j))

        push(0,0)
        while queue and len(res) < k:
            print(queue)
            sum,i,j = heapq.heappop(queue)
            res.append([nums1[i],nums2[j]])
            push(i,j+1)

            if j == 0:
                push(i+1,j)

        return res
    







nums1 = [1,1,11]
nums2 = [2,4,6]

k = 10

s = Solution()

print(s.kSmallestPairs(nums1,nums2,k))