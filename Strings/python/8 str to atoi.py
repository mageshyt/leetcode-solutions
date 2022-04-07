import re
from turtle import pen

class Solution:
    def myAtoi(self, s: str) -> int:
        min=pow(-2,31)
        max=pow(2,31)
        s=s.strip()
        reg=re.compile(r'^[-+]?\d+')
        if re.match(reg,s):
            if(int(s)>max):
                return max
            elif(int(s)<min):
                return min
        else:
            return 0
        return int(s)

ex1=Solution()
res=ex1.myAtoi("-123")
print(res)
        