from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) == 0 or len(nums2) == 0:
            return -1

        nums1 = set(nums1)
        nums2 = set(nums2)

        common = nums1.intersection(nums2)
        print(common)

        if len(common) == 0:
            return -1

        return min(common)

    def getCommon2(self, nums1: List[int], nums2: List[int]) -> int:
        l1 = 0
        l2 = 0

        r = min(len(nums1), len(nums2))

        while l1 < r and l2 < r:
            if nums1[l1] == nums2[l2]:
                return nums1[l1]
            if nums1[l1] < nums2[l2]:
                l1 += 1
            else:
                l2 += 1

        if l1 < len(nums1) :
            return nums1[l1] if nums1[l1] in nums2 else -1
        
        if l2 < len(nums2):
            return nums2[l2] if nums2[l2] in nums1 else -1
        
        return -1


print(Solution().getCommon2([1, 1, 2], [3, 4]))
