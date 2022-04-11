class Solution:
    def rotate(self, nums, k) :
        for i in range(k):
            nums[:] = nums[-1:] + nums[:-1]
            print('After -->', nums)
        return nums

test=Solution()
print(test.rotate([1,2,3,4,5,6,7],3))
