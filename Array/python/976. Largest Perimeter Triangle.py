'''Given an integer array nums, return the largest perimeter of a triangle 
    with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

 

Example 1:

Input: nums = [2,1,2]
Output: 5
Example 2:

Input: nums = [1,2,1]
Output: 0'''


class Solution:
    def largestPerimeter(self, nums ) :

        max_area = 0
        nums.sort(reverse=True)
        print(nums)
        for i in range(len(nums) - 2):
            # sum of two side need to be greatear than another side
            if nums[i] < nums[i + 1] + nums[i + 2]:
                max_area = nums[i] + nums[i + 1] + nums[i + 2]
                break
        return max_area


test=Solution()
print(test.largestPerimeter([2,1,2]))