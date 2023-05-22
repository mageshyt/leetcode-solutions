"""Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]"""


class Solution:
    def topKFrequent(self, nums, k):
        map = Counter(nums)
        result = []  # [num , count]
        for key, value in map.items():
            result.append([key, value])
        result.sort(key=lambda x: x[1], reverse=True)

        return [res[0] for res in result[:k]]

