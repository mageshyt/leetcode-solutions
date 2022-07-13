class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands=0
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        visited=set()
        rows=len(grid)
        cols=len(grid[0])

        def dfs(r,c):
            if (r,c ) in visited:
                return
            visited.add((r,c))

            for (dx,dy) in directions:
                newRow=r+dx
                newCol=c+dy
                if newRow>=0 and newRow<rows and newCol>=0 and newCol<cols and grid[newRow][newCol]=='1':
                    dfs(newRow,newCol)
                    
                    



        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                    self.dfs(grid,r,c,directions)
                    islands+=1