import heapq


class Solution:
    def findKthLargest(self, nums , k: int) -> int:
        min_heap=[]
        for num in nums:
            heapq.heappush(min_heap,-num)
        res=-1
        while k:
            k-=1
            res= -heapq.heappop(min_heap)
        return res 
             
if __name__ == "__main__":
    nums =  [3,2,3,1,2,4,5,5,6]
    k = 4
    sol = Solution()
    print(sol.findKthLargest(nums,k))
        