'''You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the sum of scores of all the players in the team.

However, the basketball team is not allowed to have conflicts. A conflict exists if a younger player has a strictly higher score than an older player. A conflict does not occur between players of the same age.

Given two lists, scores and ages, where each scores[i] and ages[i] represents the score and age of the ith player, respectively, return the highest overall score of all possible basketball teams.

 

Example 1:

Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
Output: 34
Explanation: You can choose all the players.
'''


class Solution:
    def bestTeamScore(self, scores, ages) -> int:
        players = sorted(zip(ages, scores))
        dp = [0] * len(players)

        for i, (age, score) in enumerate(players):
            dp[i] = score

            for j in range(i):

                if players[j][1] <= score:
                    dp[i] = max(dp[i], dp[j] + score)

        return max(dp)


if __name__ == '__main__':
    scores = [1, 3, 5, 10, 15]
    ages = [1, 2, 3, 4, 5]
    print(Solution().bestTeamScore(scores, ages))
