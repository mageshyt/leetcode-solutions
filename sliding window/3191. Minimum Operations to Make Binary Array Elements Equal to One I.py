"""

You are given a binary array nums.

You can do the following operation on the array any number of times (possibly zero):

Choose any 3 consecutive elements from the array and flip all of them.
Flipping an element means changing its value from 0 to 1, and from 1 to 0.

Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.
Example 1:

Input: nums = [0,1,1,1,0,0]

Output: 3

Explanation:
We can do the following operations:

Choose the elements at indices 0, 1 and 2. The resulting array is nums = [1,0,0,1,0,0].
Choose the elements at indices 1, 2 and 3. The resulting array is nums = [1,1,1,0,0,0].
Choose the elements at indices 3, 4 and 5. The resulting array is nums = [1,1,1,1,1,1].
Example 2:

Input: nums = [0,1,1,1]

Output: -1

Explanation:
It is impossible to make all elements equal to 1.

 

Constraints:

3 <= nums.length <= 105
0 <= nums[i] <= 1

"""

from typing import List
from collections import deque 
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # base case
        if len(nums) < 3:
            return -1
        count = 0
        flip_bits = deque()

        for i in range(len(nums)):
            # if the ith element is 0 and the length of flip_bits is less than 2
            while flip_bits and i > flip_bits[0]+2:
                flip_bits.popleft()

            if (nums[i] + len(flip_bits)) % 2 == 0:
                if i +2 >= len(nums):
                    return -1
                count += 1
                flip_bits.append(i)
        return count

print(Solution().minOperations([0,1,1,1,0,0])) #3
print(Solution().minOperations([0,1,1,1])) #-1
