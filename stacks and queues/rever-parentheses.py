class Solution:
    def reverseParentheses(self, s: str) -> str:
        res=[]

        for i in s:
            # if the character is closing bracket, then pop the elements until opening bracket is found
            if i==")":
                temp=[]
                while res[-1]!="(":
                    temp.append(res.pop())
                res.pop()
                res+=temp
            else:
                # append the character to the result
                res.append(i)

        print(res)
        return "".join(res)




print(Solution().reverseParentheses("(ed(et(oc))el)"))
