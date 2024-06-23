"""Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

 

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.
Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
0 <= limit <= 109"""

from typing import List
from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        # Sliding window with min and max queue

        min_queue = deque()
        max_queue = deque()

        left = 0

        for right in range(len(nums)):
            # update min_queue
            while min_queue and nums[right]< min_queue[-1]:
                min_queue.pop()

            min_queue.append(nums[right])

            # update max_queue

            while max_queue and nums[right]> max_queue[-1]:
                max_queue.pop()

            max_queue.append(nums[right])

            # check if the window is valid 
                # valid : if the max value - min value is greater than limit then we need to shrink the window

            if max_queue[0] - min_queue[0] > limit:

                if min_queue[0] == nums[left]:
                    min_queue.popleft()

                if max_queue[0] == nums[left]:
                    max_queue.popleft()

                left += 1

        return right - left + 1
    
# Time complexity: O(n)
# Space complexity: O(n)

print(Solution().longestSubarray([8,2,4,7], 4)) # 2

print(Solution().longestSubarray([10,1,2,4,7,2], 5)) # 4


        