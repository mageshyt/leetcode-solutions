"""

You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.

A 0-indexed string num of length n + 1 is created using the following conditions:

num consists of the digits '1' to '9', where each digit is used at most once.
If pattern[i] == 'I', then num[i] < num[i + 1].
If pattern[i] == 'D', then num[i] > num[i + 1].
Return the lexicographically smallest possible string num that meets the conditions.

 

Example 1:

Input: pattern = "IIIDIDDD"
Output: "123549876"
Explanation:
At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
Some possible values of num are "245639871", "135749862", and "123849765".
It can be proven that "123549876" is the smallest possible num that meets the conditions.
Note that "123414321" is not possible because the digit '1' is used more than once.
Example 2:

Input: pattern = "DDD"
Output: "4321"
Explanation:
Some possible values of num are "9876", "7321", and "8742".
It can be proven that "4321" is the smallest possible num that meets the conditions.
"""
class Solution:
    # stack Solution
    def smallestNumber(self, pattern: str) -> str:
        n=len(pattern)

        res,stack=[],[]

        for i in range(n+1):
            stack.append(i+1)
            if i==n or pattern[i]=="I":
                while stack:
                    res.append(str(stack.pop()))


        return "".join(res)


    # backtraack


    def smallestNumber(self,pattern):
        n=len(pattern)
        res=[]
        used=set()
        def backtrack(idx,current):
            # GOAL
            if len(current) == n+1:
                res.append("".join(current))
                return True

            # CHOICE

            for digit in "123456789":
                # if already user
                if digit in used:
                    continue

                if current and pattern[idx-1]=="I" and current[-1]>=digit:
                    continue

                if current and pattern[idx-1]=="D" and current[-1]<=digit:
                    continue

                # ACTION

                used.add(digit)
                current.append(digit)
                # RECURSE

                if backtrack(idx+1,current):
                    return True

                # BACKTRACK

                current.pop()
                used.remove(digit)


            return False


        backtrack(0,[])
        return res[0]


s=Solution()

print(s.smallestNumber("D")) # 21
print(s.smallestNumber("IIIDIDDD")) # 21
