"""
You are given a list of strings of the same length words and a string target.

Your task is to form target using the given words under the following rules:

target should be formed from left to right.
To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every string.
Repeat the process until you form the string target.
Notice that you can use multiple characters from the same string in words provided the conditions above are met.

Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: words = ["acca","bbbb","caca"], target = "aba"
Output: 6
Explanation: There are 6 ways to form target.
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")
Example 2:

Input: words = ["abba","baab"], target = "bab"
Output: 4
Explanation: There are 4 ways to form target.
"bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
"bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
"bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
"bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")

"""

from typing import List
from collections import defaultdict
class Solution:
    # Top down approach
    def numWays(self, words: List[str], target: str) -> int:
        dp =  { } # (idx1,idx2)
        n,m=len(words),len(target)
        cnt=defaultdict(int) # (idx,char):count

        for word in words:
            for idx,char in enumerate(word):
                cnt[(idx,char)]+=1

        def dfs(idx1,idx2):
            if idx2==m:
                return 1

            if idx1==len(words[0]): 
                return 0

            if (idx1,idx2) in dp:
                return dp[(idx1,idx2)]

            skip=dfs(idx1+1,idx2) # skip the current word
            take=cnt[(idx1,target[idx2])]*dfs(idx1+1,idx2+1)

            dp[(idx1,idx2)]=skip+take

            return dp[(idx1,idx2)]

        return dfs(0,0)%(10**9+7)

s=Solution()
words = ["acca","bbbb","caca"]
target = "aba"

print(s.numWays(words,target))
print(s.numWays2(words,target))


