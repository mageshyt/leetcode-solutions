"""Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

"""


class Solution:
    def minFallingPathSum(self, matrix) -> int:
        # logic lets go from bottom to top

        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(1,rows):
            for c in range (cols):

                mid=matrix[r-1][c]
                left=matrix[r-1][c-1] if c>0 else float('inf')
                right=matrix[r-1][c+1] if c<cols-1 else float('inf')
                print(mid,left,right)
                matrix[r][c]+=min(mid,left,right)

        return min(matrix[-1])
    

    def minFallingPathSum(self, matrix) -> int:
        cache={}
        rows=len(matrix)
        cols=len(matrix[0])

        def dfs(row,col):
            # base case 
            if col <0 or col>=cols:
                return float('inf') 
            # 1. if row is out of bound
            if row==rows-1:
                return matrix[row][col]
            
            if (row,col) in cache:
                return cache[(row,col)]
            
            # logic 
            cache[(row,col)]=matrix[row][col]+min(dfs(row+1,col-1),dfs(row+1,col),dfs(row+1,col+1))
            return cache[(row,col)]
        
        min_val=float('inf')

        for col in range(cols):
            min_val=min(min_val,dfs(0,col))


        return min_val
            







if __name__ == '__main__':
    sol = Solution()
    print(sol.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
