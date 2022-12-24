'''Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''


class Solution:
    def longestConsecutive(self, nums) -> int:

        num_set = set(nums)

        max_len = 0
        for num in num_set:
            # check if num - 1 is in num_set, if not, then num is the start of a consecutive sequence
            if num - 1 not in num_set:
                cur_num = num
                cur_len = 1
                while cur_num + 1 in num_set:
                    cur_num += 1
                    cur_len += 1

                max_len = max(max_len, cur_len)
        return max_len
