from typing import List
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total = mean * (m + n) # total sum of all rolls
        missing = total - sum(rolls) # sum of all missing rolls
        print(missing)

        if missing < n or missing > 6 * n: return []
        print(missing)

        res = [] 

        while missing :
            dic=min(6, missing - n + 1) # be greedy, try to get the maximum number

            res.append(dic)
            missing -= dic # update the missing sum
            n -= 1


        return res

        print(res)



print(Solution().missingRolls([3,2,4,3], 4, 2)) # [6,6]





