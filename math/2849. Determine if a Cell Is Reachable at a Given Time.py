class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        # Calculate the width and height differences between the starting (sx, sy) and ending (fx, fy) points.
        width = abs(sx - fx)
        height = abs(sy - fy)

        # Check if the starting and ending points are the same and t is 1, which would not allow reaching the same point again.
        if width == 0 and height == 0 and t == 1:
            return False
        
        # Check if the given time t is greater than or equal to the maximum of width and height.
        # If t is greater, it's possible to reach the destination in the given time.
        return t >= max(width, height)

if __name__ == "__main__":
    s=Solution()

    print(s.isReachableAtTime(3,1,7,3,3))
















































 











