"""Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.
Example 3:
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
 

"""

from typing import List
from collections import deque, defaultdict
class Solution:
    # Time complexity: O(N) | Space complexity: O(N)
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        odd = deque([-1])
        res=0
        for i in range(n):
            if nums[i] % 2 != 0:
                odd.append(i)

            if len(odd) > k + 1:
                odd.popleft()

            if len(odd) == k + 1:
                res += odd[1] - odd[0]

        return abs(res)
    
print(Solution().numberOfSubarrays([1,1,2,1,1], 3)) # 2
print(Solution().numberOfSubarrays([2,4,6], 1)) # 0
print(Solution().numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2)) # 16



    
