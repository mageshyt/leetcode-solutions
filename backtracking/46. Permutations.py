class Solution:
    def permute(self, nums):
        res = []
        self.backtrack(nums, [], res)
        print(res)
        return res

    def backtrack(self, nums, path, res):
        if not nums:
            res.append(path)
            return

        for i in range(len(nums)):
            self.backtrack(nums[:i] + nums[i+1:], path + [nums[i]], res)


# Path: backtracking/47. Permutations II.py

if __name__ == "__main__":
    nums = [1,  2, 3]
    Solution().permute(nums)
