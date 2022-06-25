'''Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.
'''

class Solution:
    def targetIndices(self, nums, target: int):
        res=[]
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                res.append(i)
        return res

if __name__=='__main__':
    s=Solution()
    print(s.targetIndices( [1,2,5,2,3],2))