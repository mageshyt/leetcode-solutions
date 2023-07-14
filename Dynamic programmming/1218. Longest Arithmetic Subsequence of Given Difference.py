import collections
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        res=0

        for i in range(len(arr)):
            count=0
            for j in range(i,len(arr)):
                if arr[j]-arr[i]==difference:
                    count+=1
                    i=j

            res=max(res,count)

        return res+1
    
    # DP solution

    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        dp = collections.defaultdict(int)
        res = 0

        for i in range(len(arr)):
            dp[arr[i]] = max(dp[arr[i]], dp[arr[i]-difference]+1)

            res = max(res, dp[arr[i]])

        return res
    



