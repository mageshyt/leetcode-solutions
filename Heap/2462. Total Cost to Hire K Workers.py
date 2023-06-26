import heapq
from typing import List
class Solution:
    def totalCost(self, costs: List[int], k: int, n: int) -> int:
        left=0
        right=len(costs)-1
        heap1=[]
        heap2=[]
        count=res=0
        while count <k:

            while (len(heap1) < n and left <= right):
                heapq.heappush(heap1,costs[left])
                left+=1

            while (len(heap2) < n and  right >= left):
                heapq.heappush(heap2,costs[right])
                right-=1

            min1=heap1[0] if len(heap1) > 0 else float('inf') # getting the min val from heap 1

            min2=heap2[0] if len(heap2) >0 else float('inf') # getting the min val from heap2

            # if both are same then according to the index val we will remove (ie from heap1 because heap have first (n) element so that idx order will be first )

            if min1 <=min2:
                res+=min1
                heapq.heappop(heap1) 
            else:
                res+=min2
                heapq.heappop(heap2) 

            count+=1

        return res



if __name__ == "__main__":
    costs = [17,12,10,2,7,2,11,20,8]
    k = 3
    n = 4
    sol = Solution()
    print(sol.totalCost(costs,k,n))
