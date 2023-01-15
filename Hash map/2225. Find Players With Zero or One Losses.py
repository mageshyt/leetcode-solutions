'''You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.
 

Example 1:

Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
Example 2:

Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].
 

Constraints:

1 <= matches.length <= 105
matches[i].length == 2
1 <= winneri, loseri <= 105
winneri != loseri
All matches[i] are unique.'''


class Solution:
    def findWinners(self, matches):
        win_set = set()
        lose_set = set()
        exact_one = {}
        for match in matches:
            win_set.add(match[0])
            lose_set.add(match[1])
            exact_one[match[1]] = exact_one.get(match[1], 0) + 1

        res = [sorted(list(win_set-lose_set))]
        for num in exact_one.keys():
            if exact_one[num] != 1:
                lose_set.remove(num)
        res.append(sorted(list(lose_set)))
        return res


if __name__ == "__main__":
    matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7],
               [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]

    print(Solution().findWinners(matches))
