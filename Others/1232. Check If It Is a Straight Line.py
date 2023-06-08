"""You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

 

 

Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 """
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # base case
        if len(coordinates) == 2:
            return True
        
        # get the slope
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        slope = (y2-y1)/(x2-x1) if x2-x1 != 0 else float('inf')

        # check if all the points are on the same line

        for i in range(2, len(coordinates)):
            x1, y1 = coordinates[i-1]
            x2, y2 = coordinates[i]
           
            if x2-x1 == 0:
                if slope != float('inf'):
                    return False
            elif (y2-y1)/(x2-x1) != slope:
                return False
            
        return True
    

