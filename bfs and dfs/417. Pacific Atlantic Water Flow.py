"""There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans."""


class Solution:
    def pacificAtlantic(self, heights):
        rows, cols = len(heights), len(heights[0])

        res = []  # result -> cells that can flow to both oceans

        pacific = set()  # cells that can flow to pacific ocean
        atlantic = set()  # cells that can flow to atlantic ocean

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, visit, prev_height):
            # if already visited, return
            if (r, c) in visit:
                return

            # out of bound, return
            if(r < 0 or r >= rows or c < 0 or c >= cols):
                return
            # if current cell is lower than previous cell, return because water cannot flow to lower cell

            curr_height = heights[r][c]
            if curr_height < prev_height:
                return

            # add new cell to visit set
            visit.add((r, c))

            # go through all 4 directions
            dfs(r+1, c, visit, curr_height)  # down
            dfs(r-1, c, visit, curr_height)  # up
            dfs(r, c+1, visit, curr_height)  # right
            dfs(r, c-1, visit, curr_height)  # left

        # go though the first and last col in first and last row

        for c in range(cols):

            dfs(0, c, pacific, 0)  # first row
            dfs(rows-1, c, atlantic, 0)  # last row

        # for every row

        for r in range(rows):

            dfs(r, 0, pacific, 0)  # first col

            dfs(r, cols-1, atlantic, 0)  # last col

        # after two loop we would have  pacific and atlantic set

        # now we need to find the intersection of two sets

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])  # add to result
        return res


if __name__ == "__main__":
    heights = [[3, 3, 3], [3, 1, 3], [0, 2, 4]]
    print(Solution().pacificAtlantic(heights))
