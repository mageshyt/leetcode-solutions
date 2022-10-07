class Solution:

    def equationsPossible(self,equation)->bool:
        roots=[i for i in range(26)]

        for eq in list(equation):
            symbol=eq[1]
            if symbol == "=":
                x=ord(eq[0])-ord("a")
                y=ord(eq[3])-ord("a")
                roots[self.find(roots,x)]=self.find(roots,y)

        for eq in list(equation):
            symbol=eq[1]
            if symbol == "!":
                x=ord(eq[0])-ord("a")
                y=ord(eq[3])-ord("a")
                if self.find(roots,x)==self.find(roots,y):
                    return False
        return True

    def find(self,roots,x):
        if roots[x]!=x:
            roots[x]=self.find(roots,roots[x])
        return roots[x]


if __name__ == '__main__':
    s=Solution()
    res=s.equationsPossible(["a==b","b!=a"])
    print(res)
