class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize left and right pointers
        left = 0
        right = len(nums) - 1

        # Perform binary search in rotated array
        while left <= right:
            mid = (left + right) // 2
            mid_element = nums[mid]
            left_element = nums[left]
            right_element = nums[right]

            # Check if we found the target
            if target == mid_element:
                return mid

            # If left side is sorted
            if left_element <= mid_element:
                # Check if the target is in the sorted part or not
                if target > mid_element or target < left_element:
                    left = mid + 1
                else:
                    right = mid - 1
            # If right side is sorted
            else:
                # Check if the target is in the sorted part or not
                if target < mid_element or target > right_element:
                    right = mid - 1
                else:
                    left = mid + 1

        # Target not found
        return -1

