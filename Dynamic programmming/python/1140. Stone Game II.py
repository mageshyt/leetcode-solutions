"""Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones.

Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.



Example 1:

Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger.
Example 2:

Input: piles = [1,2,3,4,5,100]
Output: 104"""


class Solution:
    def stoneGameII(self, piles) -> int:
        # Logic
        # here both are playing optimally
        # always try to maximize the score of the current player
        # M = 1
        # Alternate turns in each turn
        dp={}

        def dfs(turn:str,i:int,m:int):

            # base case
            if i >= len(piles):
                return 0

            if (turn,i,m) in dp:
                return dp[(turn,i,m)]

            # Assume both are playing optimally
            total=0
            res=0 if turn=="Alice" else float('inf')

            for x in range(1,2*m+1): # x will be in the range of 1 < x < 2M

                if i+x > len(piles):
                    break

                total+=piles[i+x-1] # add the current pile

                if turn=="Alice":
                    res=max(res,total+dfs("Bob",i+x,max(m,x)))

                else:
                    res=min(res,dfs("Alice",i+x,max(m,x)))

            dp[(turn,i,m)]=res

            return res

        return dfs("Alice",0,1)

# Path: Dynamic programmming/python/1143. Longest Common Subsequence.py


if __name__ == "__main__":
    s = Solution()

    print(s.stoneGameII([2, 7, 9, 4, 4]))
