class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        res=0

        rows=len(grid)
        cols=len(grid[0])

        # logic

        # first be go from left to right from each row 
        # when we encounter a negative number we know that all the numbers to the right of it are negative

        # so we can add the number of elements to the right of it to the result


        for i in range(rows):
            for j in range(cols):
                if grid[i][j]<0:
                    res+=(cols-j)
                    break

        return res
    