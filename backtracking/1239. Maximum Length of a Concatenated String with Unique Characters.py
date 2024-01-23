from typing import List
from collections import Counter
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        charSet=set()

        def overlap(charSet,word):
           c=Counter(charSet) + Counter(word)
           # if any value in c is greater than 1, then there is overlap
           return max(c.values()) > 1
       
        def backtrack(i):
           # base case
            if i == len(arr):
               return len(charSet)
           
              # recursive case

            if not overlap(charSet, arr[i]):
                for c in arr[i]:
                    charSet.add(c)
                # choose
                res = backtrack(i+1)
                # unchoose
                for c in arr[i]:
                    charSet.remove(c)
            else:
                res = backtrack(i+1)
            return res
        return backtrack(0)
    

if __name__ == "__main__":
    arr = ["un","iq","ue"]
    print(Solution().maxLength(arr))
    print(f"Correct Answer is: 4")