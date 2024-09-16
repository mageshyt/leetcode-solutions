from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        timePoints.sort()
        print(timePoints)
        minDiff = (
            self.diff(timePoints[0], timePoints[-1])
        )
        # sort the timePoints

        for i in range(len(timePoints)-1):
            minDiff = min(minDiff, self.diff(timePoints[i], timePoints[i+1]))
        return minDiff

    def diff(self, t1, t2):
        h1, m1 = map(int, t1.split(':'))
        h2, m2 = map(int, t2.split(':'))

        if h1 ==0:
            h1 = 24
        if h2 ==0:
            h2 = 24

        # find the absolute difference in minutes
        diff = abs((h1*60 + m1) - (h2*60 + m2))

        return min(diff, 1440-diff)







# print(Solution().findMinDifference(["23:59","00:00","00:00"])) # 0
# print(Solution().findMinDifference(["23:59","00:00"])) # 1
print(Solution().findMinDifference(["00:00","04:00","22:00"] )) # 1

print(Solution().diff("12:12", "00:13")) # 1
# print(Solution().diff("13:59", "15:00")) # 1
# print(Solution().diff("13:59", "15:59")) # 2
