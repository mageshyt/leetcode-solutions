def subArraySum(nums, k):
    if(len(nums) == 0):
        return 0
    if (len(nums) < k):
        return 0
    windowSum =  0
    windowStart = 0
    res=[]

    for windowEnd in range(len(nums)):
        size=windowEnd-windowStart+1
        if  size<k:
            windowSum+=nums[windowEnd]
        elif size==k:
            windowSum+=nums[windowEnd]
            res.append(windowSum)
            windowSum-=nums[windowStart]
            windowStart+=1
    print(res)


subArraySum([1,2,3,4,5,6],3)



