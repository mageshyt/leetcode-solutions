

class Solution:
    def singleNonDuplicate(self, nums):
        left = 0
        right = len(nums)-1

        while left < right:
            mid = left + (right-left)//2

            neighbor = mid+1 if mid % 2 == 0 else mid-1
            if nums[mid] == nums[neighbor]:
                left = mid+1

            else:
                right = mid

        return nums[left]


if __name__ == "__main__":
    nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]

    print(Solution().singleNonDuplicate(nums))
