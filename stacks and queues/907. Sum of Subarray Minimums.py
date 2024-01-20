
from typing import List
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # Time: O(n) | Space: O(n)
        MOD=10**9+7

       # right boundary of i, where arr[i] is the minima.
        leftToRight = [len(arr)] * len(arr)
        
        # going from left to right to find the right boundary.
        stack = []
        for i in range(len(arr)):
            while stack and arr[i] <= arr[stack[-1]]:
                leftToRight[stack.pop()] = i
            stack.append(i)
        
        # Left boundary of i, where arr[i] is the minima.
        rightToLeft = [-1] * len(arr)
        # going from right to left to find the left boundary.
        stack = [] # resetting the stack 
        for i in reversed(range(len(arr))):
            while stack and arr[i] < arr[stack[-1]]:
                # if the current element is smaller than the top of the stack, pop the stack
                rightToLeft[stack.pop()] = i 
            stack.append(i)

        res = 0
        
        for idx in range(len(arr)):
            left, right = rightToLeft[idx], leftToRight[idx]
            res += (right-idx) * (idx-left) * arr[idx]
            res %= MOD
            
        return res

 

    
print(Solution().sumSubarrayMins([3,1,2,4]))