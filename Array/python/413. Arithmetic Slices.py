class Solution:
    def numberOfArithmeticSlices(self, nums) :
        result=0
        count=0
        for i in range(0,len(nums)):
            if i+1 < len(nums) :
                diff_1=nums[i] -nums[i+1]

            if i+1 < len(nums) and i+2 < len(nums) :
                diff_2=nums[i+1] - nums[i+2]
            if diff_2 == diff_1:
                count+=1
                result+=count
            else:
                count=0
        return result
            
test=Solution()
print(test.numberOfArithmeticSlices([1,2,3,4]))