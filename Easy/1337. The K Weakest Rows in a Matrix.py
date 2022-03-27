class Solution:
    def kWeakestRows(self, mat, k) :
        res=[]
        for i in range(len(mat[0])):
            print(i)
        print(res)   
           
test=Solution()
mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
print(test.kWeakestRows(mat,3))

