from math import sqrt
class Solution:
    # Time complexity: O(sqrt(c))
    # Space complexity: O(1)
    def judgeSquareSum(self, c: int) -> bool:
        
        end=int(sqrt(c))
        start=0

        def dfs(start,end,c):
            # base case
            if start > end:
                return False
            # recursive case
            if start**2 + end**2 == c:
                return True
            elif start**2 + end**2 < c:
                return dfs(start+1,end,c)
            else:
                return dfs(start,end-1,c)
            
        return dfs(start,end,c)
    
    def judgeSquareSum(self, c: int) -> bool:
        start=0
        end=int(sqrt(c))
        while start <= end:
            if start**2 + end**2 == c:
                return True
            elif start**2 + end**2 < c:
                start+=1
            else:
                end-=1
        return False


print(Solution().judgeSquareSum(3))

    