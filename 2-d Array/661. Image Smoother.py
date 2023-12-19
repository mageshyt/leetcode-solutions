
from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # Time: O(m*n)  Space: O(m*n)

        # 1. get the number of rows and cols
        rows, cols = len(img), len(img[0])
        res = [[0] * cols for _ in range(rows)]

        # 2. iterate through the matrix
        for i in range(rows):
            for j in range(cols):
                # 3. get the average of the cell
                res[i][j] = self.getAvg(img, i, j, rows,cols)
        return res
    
    def getAvg(self,img,r,c,rows,cols):
        dirs = [[0,0],[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]] # 8 directions

        isBoundary = lambda x,y: x < 0 or y < 0 or x >= rows or y >= cols   # check if the cell is boundary

        sum, count = 0, 0

        for d in dirs:
            newRow,newCol=r+d[0],c+d[1]
            if not isBoundary(newRow,newCol):
                sum += img[newRow][newCol]
                count += 1  

        return sum // count
    


if __name__ == "__main__":
    sol = Solution()
    img = [[100,200,100],[200,50,200],[100,200,100]]
    print(sol.imageSmoother(img))
        