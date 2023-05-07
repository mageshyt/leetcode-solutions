class Solution:
    def findDifference(self, nums1, nums2):
        distinct1 = set(nums1) - set(nums2)
        distinct2 = set(nums2) - set(nums1)

        return [list(distinct1), list(distinct2)]


if __name__ == '__main__':
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]
    instance = Solution()
    solution = instance.findDifference(nums1, nums2)
    print(solution)
