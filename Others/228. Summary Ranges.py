class Solution:
    def summaryRanges(self, nums):
        res = []

        if len(nums) == 0:
            return res

        left = 0
        right = 1

        while right < len(nums):

            # if both have difference of 1 then move right

            if nums[right] - nums[right-1] == 1:
                right += 1

            # if difference is not 1 then add to res and move left and right

            else:
                if left == right-1:
                    res.append(str(nums[left]))
                else:
                    res.append(str(nums[left]) + "->" + str(nums[right-1]))
                left = right
                right += 1

        # for last element

        if left == right-1:
            res.append(str(nums[left]))

        else:
            res.append(str(nums[left]) + "->" + str(nums[right-1]))

        return res


nums = [0, 1, 2, 4, 5, 7]

ob = Solution()

print(ob.summaryRanges(nums))
