class Solution:
    def reverseParentheses(self, s: str) -> str:
        res=[]

        for i in s:
            if i==")":
                temp=[]
                while res[-1]!="(":
                    temp.append(res.pop())
                res.pop()
                res+=temp
            else:
                res.append(i)

        print(res)
        return "".join(res)




print(Solution().reverseParentheses("(ed(et(oc))el)"))
