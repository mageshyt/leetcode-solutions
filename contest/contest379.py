
from typing import List
import math
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        
        diagonalLength=[]
        maxDiagonalLength=0

        for idx,(w1,h1) in enumerate(dimensions):
            CurrdiagonalLength=math.sqrt(w1**2+h1**2)

            currentArea=w1*h1
            maxDiagonalLength=max(maxDiagonalLength,CurrdiagonalLength)
            diagonalLength.append((CurrdiagonalLength,currentArea))


        maxArea=0
        for diagonalLength,area in diagonalLength:
            if diagonalLength == maxDiagonalLength:
                maxArea=max(maxArea,area)

        return maxArea
    


print(Solution().areaOfMaxDiagonal([[9,3],[8,6]]))



from collections import deque

class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        if a == e:
            if c != a: return 1
            if not b < d < f and not f < d < b: return 1
        if b == f:
            if d != b: return 1
            if not a < c < e and not e < c < a: return 1
        
        dx, dy = e - c, f - d
        if abs(dx) != abs(dy): return 2
        dx //= abs(dx)
        dy //= abs(dy)
        
        x, y = c, d
        while (x, y) != (e, f):
            x += dx
            y += dy
            if (x, y) == (a, b): return 2
        return 1








    
print(Solution().minMovesToCaptureTheQueen(1, 1, 8, 8,2,3))



#100150. Maximum Size of a Set After Removals


class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        removeElements = n//2
        # remove duplicates
        normalizedSet1 = set(nums1)
        normalizedSet2 = set(nums2)



        if len(normalizedSet1 - normalizedSet2) >=removeElements:
            # if we remove all elements in x2, we can get n//2 elements
            return removeElements + min(len(normalizedSet2), removeElements)
        if len(normalizedSet2 - normalizedSet1) >= removeElements:
            # if we remove all elements in x1, we can get n//2 elements
            return removeElements + min(len(normalizedSet1),removeElements)
        
        a, b = len(normalizedSet1 - normalizedSet2), len(normalizedSet2 - normalizedSet1)
        c = len(normalizedSet1 & normalizedSet2)
        return min(a + b + c, n)


print(Solution().maximumSetSize([1,2],
[9,2]
))
            

        
