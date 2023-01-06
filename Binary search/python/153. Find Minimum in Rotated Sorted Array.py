'''Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
'''


class Solution:
    def findMin(self, num):

        if len(num) <= 1:
            return num[0]

        left, right = 0, len(num)-1

        if num[left] < num[right]:
            return num[0]

        while left < right:
            mid = (left+right)//2

            # check mid val is greater than mid+1 val
            if num[mid] > num[mid+1]:
                return num[mid+1]
            # check mid val is less than mid-1 val
            elif num[mid] < num[mid-1]:
                return num[mid]
            # check mid val is greater than left val
            elif num[mid] > num[left]:
                left = mid+1
            # check mid val is less than right val
            elif num[mid] < num[right]:
                right = mid-1
        return num[left]

    def mySolution(self, nums):
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = 0

        # base case 1  if left value if less than right means then left is min of all

        if nums[left] < nums[right]:
            return nums[left]

        while left <= right:
            mid = (left+right)//2

            # if mid_value is > than mid next value then we have to move the left point

            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid] < nums[mid-1]:
                return nums[mid]

            elif nums[mid] < nums[left]:
                # if mid is less than mid next mean then we have to move the left point next to it
                left = mid+1

            elif nums[mid] < nums[right]:
                right = mid - 1
        return nums[left]


if __name__ == '__main__':
    num = [2, 3, 4, 5, 1]
    print(Solution().findMin(num))
