"""You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""
from typing import List
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []  # Max heap to store the elements
        res = []   # List to store the maximum values for each window
        
        for i in range(len(nums)):
            # Push the negative of the element and its index into the heap
            heapq.heappush(heap, (-nums[i], i))
            
            # If the current index is at least k-1 (reached the window size)
            if i >= k - 1:
                # Remove elements that are out of the current window
                while heap and heap[0][1] <= i - k:
                    heapq.heappop(heap)
                
                # Append the maximum value of the current window to the result list
                res.append(-heap[0][0])
        
        return res
  

nums = [1,3,-1,-3,5,3,6,7]
k = 3

print(Solution().maxSlidingWindow(nums,k))

