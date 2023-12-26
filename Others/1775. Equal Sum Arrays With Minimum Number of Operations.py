
"""You are given two arrays of integers nums1 and nums2, possibly of different lengths. The values in the arrays are between 1 and 6, inclusive.

In one operation, you can change any integer's value in any of the arrays to any value between 1 and 6, inclusive.

Return the minimum number of operations required to make the sum of values in nums1 equal to the sum of values in nums2. Return -1​​​​​ if it is not possible to make the sum of the two arrays equal.

 

Example 1:

Input: nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
- Change nums2[0] to 6. nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2].
- Change nums1[5] to 1. nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2].
- Change nums1[2] to 2. nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2].
Example 2:

Input: nums1 = [1,1,1,1,1,1,1], nums2 = [6]
Output: -1
Explanation: There is no way to decrease the sum of nums1 or to increase the sum of nums2 to make them equal.
Example 3:

Input: nums1 = [6,6], nums2 = [1]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed. 
- Change nums1[0] to 2. nums1 = [2,6], nums2 = [1].
- Change nums1[1] to 2. nums1 = [2,2], nums2 = [1].
- Change nums2[0] to 4. nums1 = [2,2], nums2 = [4]."""

from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum1,sum2=sum(nums1),sum(nums2)
        # 1. if both are equal, then we don't need to do anything so return 0
        if sum1==sum2:
            return 0
        
        # 2. find the larger and smaller array
        larger,smaller=(nums1,nums2) if sum1>sum2 else (nums2,nums1)

        # 3. get the difference between the two sums
        target=abs(sum1-sum2)

        # 4. now get the largest difference and smallest difference 
        largest_gain=[num-1 for num in larger]
        smallest_gain=[6-num for num in smaller]

        gain=largest_gain+smallest_gain

        # 5. sort the gain array in descending order
        gain.sort(reverse=True)

        count=0

        for num in gain:
            target-=num
            count+=1
            if target<=0:
                return count
            
        return -1
    

