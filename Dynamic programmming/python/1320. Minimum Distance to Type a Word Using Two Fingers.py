"""
You have a keyboard layout as shown above in the X-Y plane, where each English uppercase letter is located at some coordinate.

For example, the letter 'A' is located at coordinate (0, 0), the letter 'B' is located at coordinate (0, 1), the letter 'P' is located at coordinate (2, 3) and the letter 'Z' is located at coordinate (4, 1).
Given the string word, return the minimum total distance to type such string using only two fingers.

The distance between coordinates (x1, y1) and (x2, y2) is |x1 - x2| + |y1 - y2|.

Note that the initial positions of your two fingers are considered free so do not count towards your total distance, also your two fingers do not have to start at the first letter or the first two letters.

 

Example 1:

Input: word = "CAKE"
Output: 3
Explanation: Using two fingers, one optimal way to type "CAKE" is: 
Finger 1 on letter 'C' -> cost = 0 
Finger 1 on letter 'A' -> cost = Distance from letter 'C' to letter 'A' = 2 
Finger 2 on letter 'K' -> cost = 0 
Finger 2 on letter 'E' -> cost = Distance from letter 'K' to letter 'E' = 1 
Total distance = 3
Example 2:

Input: word = "HAPPY"
Output: 6
Explanation: Using two fingers, one optimal way to type "HAPPY" is:
Finger 1 on letter 'H' -> cost = 0
Finger 1 on letter 'A' -> cost = Distance from letter 'H' to letter 'A' = 2
Finger 2 on letter 'P' -> cost = 0
Finger 2 on letter 'P' -> cost = Distance from letter 'P' to letter 'P' = 0
Finger 1 on letter 'Y' -> cost = Distance from letter 'A' to letter 'Y' = 4
Total distance = 6
 

Constraints:

2 <= word.length <= 300
word consists of uppercase English letters.
"""


class Solution:
    def minimumDistance(self, word: str) -> int:
        layout = [
            (0,0), (0,1) ,(0,2),(0,3),(0,4),(0,5),
            (1,0), (1,1) ,(1,2),(1,3),(1,4),(1,5),
            (2,0), (2,1) ,(2,2),(2,3),(2,4),(2,5),
            (3,0), (3,1) ,(3,2),(3,3),(3,4),(3,5),
            (4,0), (4,1) ,(4,2),(4,3),(4,4),(4,5)
        ]

        dp = {}

        def dfs(i, f1, f2):
            if i == len(word):
                return 0

            if (i, f1, f2) in dp:
                return dp[(i, f1, f2)]

            idx = ord(word[i]) - ord('A')
            cost1 = 0 if f1 == -1 else abs(layout[f1][0] - layout[idx][0]) + abs(layout[f1][1] - layout[idx][1])
            cost2 = 0 if f2 == -1 else abs(layout[f2][0] - layout[idx][0]) + abs(layout[f2][1] - layout[idx][1])

            dp[(i, f1, f2)] = min(cost1 + dfs(i + 1, idx, f2), cost2 + dfs(i + 1, f1, idx))
            return dp[(i, f1, f2)]


        return dfs(0, -1, -1)

       

