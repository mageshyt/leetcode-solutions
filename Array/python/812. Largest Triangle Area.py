

class Solution:
    def largestTriangleArea(self, points) :
        height = 0
        width= 0
        for point in points :
            [x,y] = point
            height = max(height,y)
            width = max(width,x)
        return height*width/2

      
test=Solution()
ans=test.largestTriangleArea([[1,0],[0,0],[0,1]])
print(ans)  