
from typing import List
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i=0
        j=len(nums)-1

        while i<j:

            isLeftEven=nums[i]%2==0
            isRightEven=nums[j]%2==0

            # case 1 : if both pointers are even then move the left pointer 
            if isLeftEven and isRightEven:
                i+=1

            # case 2 : if both pointers are odd then move the right pointer
            elif not isLeftEven and not isRightEven:
                j-=1

            # case 3 : if left pointer is odd and right pointer is even then swap
            elif not isLeftEven and isRightEven:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1

            # case 4 : if left pointer is even and right pointer is odd then move both pointers
            else:
                i+=1
                j-=1

        return nums
    

if __name__ == "__main__":
    nums=[3,1,2,4]
    print(Solution().sortArrayByParity(nums)) #[2,4,3,1]


        