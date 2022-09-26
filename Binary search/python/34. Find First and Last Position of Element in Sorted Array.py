class Solution:
    def searchRange(self, nums, target: int) :
        if not nums: return [-1, -1]

        res=[]

        def binarySearch(target,left,right):
            while left <= right:
                mid=left+(right-left)//2
                if nums[mid]==target:
                    return mid
                if nums[mid]>target:
                    right=mid-1
                else:
                    left=mid+1
            return -1
        firstIdx=binarySearch(target,0,len(nums)-1)
        if firstIdx == -1 :
            return [-1,-1]

        start=firstIdx

        end=firstIdx

        temp1=0

        while start != -1:
            temp1=start
            start=binarySearch(target,0,temp1-1)
        
        start=temp1

        temp2=0
        while end != -1:
            temp2=end
            end=binarySearch(target,temp2+1,len(nums)-1)

        return  [temp1,temp2]



s=Solution()
print(s.searchRange([5,7,7,8,8,10],8))

print(s.searchRange([5,7,7,8,8,10],6))
       