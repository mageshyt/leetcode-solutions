'''Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.'''

import math

class Solution:
    def findMedianSortedArrays(self, nums1 , nums2 ) -> float:
        merged=self.merge(nums1,nums2)
        mid=len(merged)//2
        if len(merged)%2==0:
            return (merged[mid]+merged[mid-1])/2

        return merged[len(merged)//2]
 


    def merge(self,arr1,arr2):
        i=0
        j=0
        res=[] # merged array

        while i < len(arr1) and j < len(arr2):
            # case 1 when arr[i] is smaller than arr2[j]

            if arr1[i] < arr2[j]:
                res.append(arr1[i]) # push the ele to res
                i+=1
            else:
                # case 2 when arr[i] is greater than arr2[j]
                res.append(arr2[j])
                j+=1

        # for left over nums
        while i < len(arr1):
            res.append(arr1[i])
            i+=1

        while j < len(arr2):
            res.append(arr2[j])
            j+=1

        return res



if __name__ == "__main__":
    arr1=[]
    arr2=[2,3]
    print(Solution().findMedianSortedArrays(arr1,arr2))

