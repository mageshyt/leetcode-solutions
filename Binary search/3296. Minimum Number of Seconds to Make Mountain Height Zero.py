"""
You are given an integer mountainHeight denoting the height of a mountain.

You are also given an integer array workerTimes representing the work time of workers in seconds.

The workers work simultaneously to reduce the height of the mountain. For worker i:

To decrease the mountain's height by x, it takes workerTimes[i] + workerTimes[i] * 2 + ... + workerTimes[i] * x seconds. For example:
To reduce the height of the mountain by 1, it takes workerTimes[i] seconds.
To reduce the height of the mountain by 2, it takes workerTimes[i] + workerTimes[i] * 2 seconds, and so on.
Return an integer representing the minimum number of seconds required for the workers to make the height of the mountain 0.
"""


from typing import List
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        left , right = 0, max(workerTimes) *( mountainHeight * (mountainHeight + 1) // 2)

        while left < right:
            mid = (left + right) // 2

            total_reduction = 0
            for time in workerTimes:
                if total_reduction >= mountainHeight:
                    break
                # Calculate how many times this worker can work in mid seconds
                # We need to solve time * (1 + 2 + ... + x) <= mid
                # This is time * (x * (x + 1) // 2) <= mid
                # Which simplifies to x * (x + 1) <= 2 * mid / time
                # We can find the maximum x using a simple loop or binary search
                low, high = 0, mountainHeight
                while low < high:
                    m = (low + high + 1) // 2
                    if (time * (m * (m + 1) // 2)) <= mid:
                        low = m
                    else:
                        high = m - 1
                total_reduction += low 

            if total_reduction >= mountainHeight:
                right = mid
            else:
                left = mid + 1

        return left



