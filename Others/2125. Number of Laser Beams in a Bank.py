

from typing import List
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res=0
        prev_row=bank[0]
        for  idx, row in enumerate(bank[1:]):
            currOne=row.count('1')
            prevOne=prev_row.count('1')


            if prevOne >0 and currOne >0:
                res+=(prevOne*currOne)
            if currOne >0:
                prev_row=row




        return res

if __name__ == "__main__":
    bank = ["011001","000000","010100","001000"]
    print(Solution().numberOfBeams(bank))