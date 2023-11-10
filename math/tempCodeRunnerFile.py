class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:

        width=abs(sx-fx)
        height=abs(sy-fy)

        print(width,height)
# Time Complexity: O(8^t)
        


if __name__ == "__main__":
    s=Solution()

    print(s.isReachableAtTime(3,1,7,3,3))
