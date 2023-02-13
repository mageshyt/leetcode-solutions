class Solution:
    def search(self, nums, target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            mid = (left+right)//2

            if target < nums[0] < nums[mid]:
                left = mid+1  # we found that target is in right side of mid

            elif target >= nums[0] > nums[mid]:
                right = mid  # we found that target is in left side of mid

            # if target is in left side of mid
            elif target > nums[mid]:
                left = mid+1

            elif target < nums[mid]:
                # if target is in right side of mid
                right = mid

            else:
                return mid

        return -1


if __name__ == '__main__':
    nums = [3, 1]
    target = 1
    print(Solution().search(nums, target))
