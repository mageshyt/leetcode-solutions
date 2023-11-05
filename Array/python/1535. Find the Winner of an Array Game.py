"""Given an integer array arr of distinct integers and an integer k.

A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0, and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.

Return the integer which will win the game.

It is guaranteed that there will be a winner of the game.

 

Example 1:

Input: arr = [2,1,3,5,4,6,7], k = 2
Output: 5
Explanation: Let's see the rounds of the game:
Round |       arr       | winner | win_count
  1   | [2,1,3,5,4,6,7] | 2      | 1
  2   | [2,3,5,4,6,7,1] | 3      | 1
  3   | [3,5,4,6,7,1,2] | 5      | 1
  4   | [5,4,6,7,1,2,3] | 5      | 2
So we can see that 4 rounds will be played and 5 is the winner because it wins 2 consecutive games.
"""
from typing import List
import collections
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:

        if k >= len(arr):
            return max(arr)
        
        wins=collections.defaultdict(int)
        left = 0
        right = 1

        res = 0
        while  right < len(arr):
            print(wins)
            if res == k:
                break

            if arr[left] > arr[right]:
                # left wins and right goes to the end
                wins[arr[left]] += 1
                if wins[arr[left]] == k:
                    return arr[left]
                arr.append(arr[right])
                arr.pop(right)

                res = max(res, wins[arr[left]])

            else:
                # right wins and left goes to the end
                wins[arr[right]] += 1
                if wins[arr[right]] == k:
                    return arr[right]
                arr.append(arr[left])
                arr.pop(left)

                res = max(res, wins[arr[right]])
        
        return res
    


        



if __name__ == "__main__":

    arr=[1,11,22,33,44,55,66,77,88,99]

    k=1000000000

    print(Solution().getWinner(arr,k))