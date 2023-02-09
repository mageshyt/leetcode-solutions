

class Solution:
    def jump(self, nums) -> int:
        # base case when there is only one element
        if len(nums) == 1:
            return 0  # no jump needed because we are already at the end

        max_steps = 0  # max steps we can take from the first position

        left = 0   # left pointer
        right = 0  # right pointer

        while (right < len(nums)-1):
            farthest = 0 # farthest we can reach from the current position

            for i in range(left, right+1):
                # calculate the farthest we can reach from the current position
                farthest = max(farthest, i + nums[i])

            left = right+1  # next left pointer
            right = farthest  # next right pointer
            max_steps += 1  # increment the result
        return max_steps


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    s = Solution()
    print(s.jump(nums))
