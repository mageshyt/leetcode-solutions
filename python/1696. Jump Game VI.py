import heapq
'''You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.

 

Example 1:

Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
Example 2:

Input: nums = [10,-5,-2,4,0,3], k = 3
Output: 17
Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
Example 3:

Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
Output: 0'''

class Solution:
    def maxResult(self, nums , k: int) -> int:
        window=[] # window
        dp=[0] * len(nums)

        for i in range(len(nums)):
            dp[i]=nums[i]
            
            if i==0:
                heapq.heappush(window,(-nums[0],0)) 
                #he reason we keep the value with minus is because python has a minheap, and we can put elements with negative sign to turn it into a max heap
                continue

            while window[0][1]< i-k:
                 #we need to discard solutions that that index lower than i-k because they became "out of range".
                heapq.heappop(window)
            dp[i] += (-window[0][0])
            heapq.heappush(window, (-dp[i], i))

        return dp[len(window)-1] #we need to return the last element of the dp array 


s=Solution()
k = 3
nums = [10,-5,-2,4,0,3]
print(s.maxResult(nums, k))