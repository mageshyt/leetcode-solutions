"""Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.

 

Example 1:

Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
Example 2:

Input: nums = [4,4,3,2,1]
Output: [[4,4]]
 

Constraints:

1 <= nums.length <= 15
-100 <= nums[i] <= 100"""


class Solution:
    def findSubsequences(self, nums):
        res = set()  # to avoid duplicates

        def dfs(nums, path):
            # only we should add the path to the result if the path has atleast 2 elements
            if len(path) >= 2:
                res.add(tuple(path))

            for i in range(len(nums)):
                # last element of the path should be less than the current element
                last = path[-1] if path else float('-inf')
                curr = nums[i]
                if nums[i] >= last:
                    # move forward
                    dfs(nums[i+1:], path+[curr])

        dfs(nums, [])
        return [list(x) for x in res]


if __name__ == "__main__":
    nums = [4, 6, 7, 7]
    print(Solution().findSubsequences(nums))
