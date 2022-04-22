class Solution:
    def combine(self, n: int, k: int) :
        res=[]
        def backtrack(first=1, comb=[]):
            print(comb)
            if(len(comb)==k):
                res.append(comb.copy())
                print(f'return {comb}')
                return
            for i in range(first,n+1):
                comb.append(i)
                backtrack(i+1,comb)
                comb.pop()
        backtrack()
        return res
test=Solution()
print(test.combine(4,2))
        