
""""""
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Check if the array is empty
        if not nums:
            return [-1, -1]

        result = []

        # Binary search helper function to find the target
        def binarySearch(target: int, left: int, right: int) -> int:
            while left <= right:
                mid = left + (right - left) // 2

                # Case 1: If the mid element is the target, return the index
                if nums[mid] == target:
                    return mid

                # Case 2: If the mid element is greater than the target, search in the left side (move right pointer)
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    # Case 3: If mid element is less than the target, search in the right side (move left pointer)
                    left = mid + 1

            # If target is not found, return -1
            return -1
    
        # Find the starting index of the target number
        firstIdx = binarySearch(target, 0, len(nums) - 1)

        # If first index is not found, return [-1, -1]
        if firstIdx == -1:
            return [-1, -1]

        endIdx = firstIdx
        start = firstIdx
        temp1 = 0

        # Find the starting index of the target number
        while start != -1:
            temp1 = start
            start = binarySearch(target, 0, temp1 - 1)

        start = temp1
        temp2 = 0

        # Find the ending index of the target number
        while endIdx != -1:
            temp2 = endIdx
            endIdx = binarySearch(target, temp2 + 1, len(nums) - 1)

        endIdx = temp2

        return [start, endIdx]




s=Solution()
print(s.searchRange([5,7,7,8,8,10],8))

print(s.searchRange([5,7,7,8,8,10],6))
       