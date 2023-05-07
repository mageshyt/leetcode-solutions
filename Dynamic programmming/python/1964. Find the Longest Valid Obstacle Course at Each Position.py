import bisect


class Solution:
    def longestObstacleCourseAtEachPosition(self, nums):
        # result[i] = height of the LOC (longest obstacle course) at i & including nums[i]
        res = []

        # dp[i] =  where i = length of the LOC ,is the smallest ending value
        dp = [float('inf')]*(len(nums)+1)

        for n in nums:
            idx = bisect.bisect(dp, n)
            print('n ', n, ' idx ', idx)
            res.append(idx+1)

            dp[idx] = n
        print(dp)
        return res


if __name__ == '__main__':
    nums = [3, 1, 5, 6, 4, 2]

    print(Solution().longestObstacleCourseAtEachPosition(nums))
