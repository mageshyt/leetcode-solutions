from collections import Counter,defaultdict
from typing import List
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        w2Map=Counter(word2)
        unique=len(w2Map)
        left,right=0,0
        result,formed=0,0
        currentWindow=defaultdict(int)
        n=len(word1)

        while right<len(word1):
            char=word1[right]
            # add the current char
            currentWindow[char]+=1

            # if we get the same window of requied 
            if char in w2Map and currentWindow[char]==w2Map[char]:
                formed+=1

            while left <=right and formed==unique:
                char=word1[left]
                result+=n-right # n-right is the length of the substring

                # remove the left char
                currentWindow[char]-=1
                if char in w2Map and currentWindow[char]<w2Map[char]:
                    formed-=1

                left+=1

            right+=1

        return result

print("TESTING VALID SUBSTRING COUNT")
s=Solution()
print(s.validSubstringCount("bcca","abc")) # 1


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        low=0
        high=max(workerTimes)*(mountainHeight*(mountainHeight+1))//2

        def helper(time):
            tot=0
            for wt in  workerTimes:
                if tot >= mountainHeight:
                    return True
                l ,h=0,mountainHeight
                while l<h:
                    mid=(l+h+1)//2
                    finishTime=(mid*(mid+1)//2)*wt
                    if finishTime<=time:
                        l=mid
                    else:
                        h=mid-1

                tot+=l
            return tot >= mountainHeight
                

        while low<high:
            mid=(low+high)//2
            if helper(mid):
                high=mid
            else:
                low=mid+1

                
        return low

print("TESTING MIN NUMBER OF SECONDS")

s=Solution()
print(s.minNumberOfSeconds(1000,[1])) # 
