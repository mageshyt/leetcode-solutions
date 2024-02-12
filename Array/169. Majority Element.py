class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1:return nums[0]
        mapreduce=Counter(nums)

        res=[float('-inf'),0] # count,key

        for k,v in mapreduce.items():
            if res[0] < v:
                res=[v,k]

        return res[1]
        