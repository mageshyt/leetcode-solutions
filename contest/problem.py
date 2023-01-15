'''Example 1:

Input: nums = [10,10,10,10,10], k = 5
Output: 50
Explanation: Apply the operation to each array element exactly once. The final score is 10 + 10 + 10 + 10 + 10 = 50.
Example 2:

Input: nums = [1,10,3,3,3], k = 3
Output: 17
Explanation: You can do the following operations:
Operation 1: Select i = 1, so nums becomes [1,4,3,3,3]. Your score increases by 10.
Operation 2: Select i = 1, so nums becomes [1,2,3,3,3]. Your score increases by 4.
Operation 3: Select i = 2, so nums becomes [1,1,1,3,3]. Your score increases by 3.
The final score is 10 + 4 + 3 = 17.
In one operation:

choose an index i such that 0 <= i < nums.length,
increase your score by nums[i], and
replace nums[i] with ceil(nums[i] / 3).
'''

import heapq
import math


class Solution:
    def maxKelements(self, nums, k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)

        res = 0
        for i in range(k):
            pop = heapq.heappop(heap)
            # perform operation
            op = math.ceil(-pop/3)

            res += pop
            heapq.heappush(heap, -op)

        return -res


if __name__ == "__main__":
    nums = [1, 10, 3, 3, 3]
    k = 3
    print(Solution().maxKelements(nums, k))


'''You are given two 0-indexed strings word1 and word2.

A move consists of choosing two indices i and j such that 0 <= i < word1.length and 0 <= j < word2.length and swapping word1[i] with word2[j].

Return true if it is possible to get the number of distinct characters in word1 and word2 to be equal with exactly one move. Return false otherwise.'''


def solve(word1, word2):
    # count the number of characters in word1 and word2
    hash_1 = set(word1)
    hash_2 = set(word2)

    print(hash_1, hash_2)

    # if the number of characters in word1 and word2 are equal
    if len(hash_1) == len(hash_2):
        return True

    # if the number of characters in word1 and word2 are not equal then we need to swap char




if __name__ == "__main__":
    word1 = "ab"
    word2 = "ba"
    s = Solution()
    print(solve(word1, word2))
