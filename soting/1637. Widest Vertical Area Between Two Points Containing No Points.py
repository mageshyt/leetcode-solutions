
from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # 1. sort the points by x
        points.sort(key=lambda x: x[0])

        # 2. find the max difference between two consecutive points

        maxDiff = 0

        for idx,point in enumerate(points[:-1]):
            x1, y1 = point    
            x2, y2 = points[idx+1]

            maxDiff = max(maxDiff, x2-x1)
        # 3. return the max difference
            
        return maxDiff  
    
