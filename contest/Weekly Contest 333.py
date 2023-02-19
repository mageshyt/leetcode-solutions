# 2570. Merge Two 2D Arrays by Summing Values


# nums-1 [id,val]  nums-2 [id,val]

# merge nums-1 and nums-2 by summing values


import math


class Solution:
    def mergeArrays(self, nums1, nums2):
        # we will use a dictionary to store the values

        dict = {}  # key = id, value = val

        for id, val in nums1:
            dict[id] = val

        for id, val in nums2:
            if id in dict:
                dict[id] += val
            else:
                dict[id] = val

        # now we have to convert the dictionary to a list of lists

        result = []

        for id, val in dict.items():
            result.append([id, val])

        # sort the result by id

        result.sort(key=lambda x: x[0])
        return result


"""You are given a positive integer n, you can do the following operation any number of times:

Add or subtract a power of 2 from n.
Return the minimum number of operations to make n equal to 0.

A number x is power of 2 if x == 2i where i >= 0.

Example 1:

Input: n = 39
Output: 3
Explanation: We can do the following operations:
- Add 20 = 1 to n, so now n = 40.
- Subtract 23 = 8 from n, so now n = 32.
- Subtract 25 = 32 from n, so now n = 0.
It can be shown that 3 is the minimum number of operations we need to make n equal to 0.
"""

# math formula to find the minimum number of operations to make n equal to 0


class Solution:
    def minOperations(self, n: int) -> int:

        pows = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512,
                1024, 2048, 4096, 8192, 16384, 32768, 65536]


s = Solution()
print(s.minOperations(39))
