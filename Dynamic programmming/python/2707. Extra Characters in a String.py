
from typing import List
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words=set(dictionary) # hash them

        cache={}

        def dfs(i):
            # base case

            if i==len(s):
                return 0
            
            if i in cache:
                return cache[i]
            
            res=len(s)-i

            res=1+dfs(i+1) # skip the char

            for j in range(i,len(s)):
                if s[i:j+1] in words:
                    # break the branch
                    res=min(dfs(j+1),res)

            cache[i]=res
            return res
        
        return dfs(0)

     