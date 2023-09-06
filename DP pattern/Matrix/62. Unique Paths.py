
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1]*n  # last rows always 1

        for i in range(m-1):  # start from second last row
            newRow = [1]*n

            for j in range(n-2, -1, -1):  # start from second last column
             
                newRow[j] = newRow[j+1]+row[j]  # add right and bottom

            row = newRow  # update row

        return row[0]  # return first element
    # recursive solution
    def uniquePaths(self,m:int,n:int)->int:
        cache={}
        def dfs(row,col):
            if (row,col)in cache:
                return cache[(row,col)]
            
            if row == 1 and col ==1:
                return 1
            
            if row==0 or col ==0:
                return 0
            
            cache[(row,col)]=dfs(row-1,col) + dfs(row,col-1)

            return cache[(row,col)]
        
        return dfs(0,0)
# Time complexity: O(2^(m+n))

# Space complexity: O(m+n)

print(Solution().uniquePaths(3, 7))
