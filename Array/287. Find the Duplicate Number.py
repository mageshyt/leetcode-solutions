'''Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3'''


class Solution:
    def findDuplicate(self, nums) -> int:
        # Floyd's Tortoise and Hare (Cycle Detection)
        # Time: O(n)
        # Space: O(1)
        turtle = 0
        hare = 0

        while True:
            turtle = nums[turtle]  # slow pointer
            hare = nums[nums[hare]]  # fast pointer
            if turtle == hare:
                break


        # phase 2

        turtle2=0
        while True:
            turtle=nums[turtle]
            turtle2=nums[turtle2]

            if turtle==turtle2:
                return turtle
            

if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2]
    print(Solution().findDuplicate(nums))
