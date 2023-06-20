from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        # base case
        if len(nums) < k:
            return [-1]

        if k <= 1:
            return nums

        windowStart = 0
        windowSum = 0
        result = [-1]*(len(nums))
        required_size = 2*k+1
        idx = 3

        for windowEnd in range(len(nums)):
            windowSum += nums[windowEnd]
            size = windowEnd-windowStart+1
            if size >= required_size:
                result[idx] = windowSum//required_size
                windowSum -= nums[windowStart]
                windowStart += 1
                idx += 1

        return result


if __name__ == "__main__":
    nums = [100000]
    k = 1
    print(Solution().getAverages(nums, k))
