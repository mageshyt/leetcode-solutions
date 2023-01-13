class Solution:
    def productExceptSelf(self, nums):
        res = [1]*len(nums)

        prefix_sum = 1

        for i, num in enumerate(nums):

            res[i] = prefix_sum

            prefix_sum *= num

        suffix_sum = 1
        print(res)

        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix_sum
            suffix_sum *= nums[i]

        return res


if __name__ == "__main__":
    print(Solution().productExceptSelf([1, 2, 3, 4]))
