"""
There exist n rectangles in a 2D plane with edges parallel to the x and y axis. You are given two 2D integer arrays bottomLeft and topRight where bottomLeft[i] = [a_i, b_i] and topRight[i] = [c_i, d_i] represent the bottom-left and top-right coordinates of the ith rectangle, respectively.

You need to find the maximum area of a square that can fit inside the intersecting region of at least two rectangles. Return 0 if such a square does not exist.

 

Example 1:


Input: bottomLeft = [[1,1],[2,2],[3,1]], topRight = [[3,3],[4,4],[6,6]]

Output: 1

Explanation:

A square with side length 1 can fit inside either the intersecting region of rectangles 0 and 1 or the intersecting region of rectangles 1 and 2. Hence the maximum area is 1. It can be shown that a square with a greater side length can not fit inside any intersecting region of two rectangles.

Example 2:


Input: bottomLeft = [[1,1],[1,3],[1,5]], topRight = [[5,5],[5,7],[5,9]]

Output: 4


"""
from typing import List

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        max_square_area = 0
        n = len(bottomLeft)

        for i in range(n):
            rect1 = [bottomLeft[i], topRight[i]]
            for j in range(i+1, n):
                rect2 = [bottomLeft[j], topRight[j]]
                if self.isBothIntercet(rect1, rect2):
                    intersect_rect = self.getIntersectRect(rect1, rect2)

                    inter_start_x, inter_start_y = intersect_rect[0]
                    inter_end_x, inter_end_y = intersect_rect[1]

                    side_length = min(inter_end_x - inter_start_x, inter_end_y - inter_start_y)

                    max_square_area = max(max_square_area, side_length * side_length)

        return max_square_area




    def isBothIntercet(self, rect1, rect2):
        s1_start_x, s1_start_y = rect1[0]
        s1_end_x, s1_end_y = rect1[1]
        s2_start_x, s2_start_y = rect2[0]
        s2_end_x, s2_end_y = rect2[1]

        if s1_start_x >= s2_end_x or s2_start_x >= s1_end_x:
            return False
        if s1_start_y >= s2_end_y or s2_start_y >= s1_end_y:    
            return False
        return True

    def getIntersectRect(self, rect1, rect2):
        s1_start_x, s1_start_y = rect1[0]
        s1_end_x, s1_end_y = rect1[1]
        s2_start_x, s2_start_y = rect2[0]
        s2_end_x, s2_end_y = rect2[1]

        inter_start_x = max(s1_start_x, s2_start_x)
        inter_start_y = max(s1_start_y, s2_start_y)
        inter_end_x = min(s1_end_x, s2_end_x)
        inter_end_y = min(s1_end_y, s2_end_y)
        
        return [[inter_start_x, inter_start_y], [inter_end_x, inter_end_y]]


    



s=Solution()

bottomLeft = [[1,1],[2,2],[3,1]]
topRight = [[3,3],[4,4],[6,6]]
print(s.largestSquareArea(bottomLeft,topRight))

print(s.getIntersectRect([[1,1],[3,3]],[[2,2],[4,4]]))

