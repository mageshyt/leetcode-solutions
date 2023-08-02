class Solution:
    def permute(self, nums):
        res = []  # List to store the final permutations

        def backTrack(path, res, nums):
            # Base case: If there are no more numbers to permute, add the current path to the result list
            if not nums:
                res.append(path)
                return
            
            # Backtracking: Try all possible permutations of the remaining numbers
            for i in range(len(nums)):
                new_nums = nums[:i] + nums[i + 1:]  # Exclude the current number from the next iteration
                backTrack(path + [nums[i]], res, new_nums)

        backTrack([], res, nums)  # Start with an empty path and the original list of numbers
        return res

if __name__ == "__main__":
    nums = [1,  2, 3]
    print(Solution().permute(nums))
