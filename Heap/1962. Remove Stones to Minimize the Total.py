'''You are given a 0-indexed integer array piles, where piles[i] represents the number of stones in the ith pile, and an integer k. You should apply the following operation exactly k times:

Choose any piles[i] and remove floor(piles[i] / 2) stones from it.
Notice that you can apply the operation on the same pile more than once.

Return the minimum possible total number of stones remaining after applying the k operations.

floor(x) is the greatest integer that is smaller than or equal to x (i.e., rounds x down).

 

Example 1:

Input: piles = [5,4,9], k = 2
Output: 12
Explanation: Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [5,4,5].
- Apply the operation on pile 0. The resulting piles are [3,4,5].
The total number of stones in [3,4,5] is 12.
Example 2:

Input: piles = [4,3,6,7], k = 3
Output: 12
Explanation: Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [4,3,3,7].
- Apply the operation on pile 3. The resulting piles are [4,3,3,4].
- Apply the operation on pile 0. The resulting piles are [2,3,3,4].
The total number of stones in [2,3,3,4] is 12.'''


import heapq


class Solution:
    def minStoneSum(self, piles, k: int):

        # 1. heapify the array
        # 2. pop the top element, reduce it by half and push it back
        # 3. repeat k times
        # 4. return the sum of the array

        # convert the array to a max heap
        # so that we can pop the largest element
        # and push it back after reducing it by half

        min_heap = []
        for pile in piles:
            heapq.heappush(min_heap, -pile)

        while k:
            k -= 1

            # pop the largest element and change its sign
            largest = -heapq.heappop(min_heap)
            # reduce it by half and push it back
            heapq.heappush(min_heap, -largest // 2)

        return sum(-x for x in min_heap)


if __name__ == "__main__":
    piles = [4, 3, 6, 7]
    k = 3
    sol = Solution()
    print(sol.minStoneSum(piles, k))
