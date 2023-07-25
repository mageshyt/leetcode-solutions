

from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # We are going to use Binary search to find the peak index in the mountain array.

        left = 0  # Initialize left pointer to the start of the array.
        right = len(arr)  # Initialize right pointer to the end of the array.

        while left < right:  # Perform binary search until left and right pointers meet.

            mid = (left + right) // 2  # Calculate the mid index.

            # If the element at mid index is greater than the element at next index (arr[mid] > arr[mid+1]),
            # it means we are on the decreasing slope of the mountain, so the peak lies to the left of mid.
            if arr[mid] > arr[mid + 1]:
                right = mid  # Move right pointer to mid.

            else:
                left = mid + 1  # Otherwise, move left pointer to the right of mid.

        return left  # Return the peak index found by binary search.


if __name__ == "__main__":
    arr=[0,1,0]
    s=Solution()
    print(s.peakINdexInMountainArray(arr))






