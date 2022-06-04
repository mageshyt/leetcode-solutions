from bisect import bisect_left


class Solution:
    def maxEnvelopes(self, envelopes) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        dp = [] 
        for w, h in envelopes:

            left=bisect_left(dp, h)

            if left == len(dp):
                dp.append(h)
            else:
                dp[left] =h 

        
        return len(dp)


# Dynamic programming/354. Russian Doll Envelopes.py
if __name__ == '__main__':
    envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
    print(Solution().maxEnvelopes(envelopes))
        