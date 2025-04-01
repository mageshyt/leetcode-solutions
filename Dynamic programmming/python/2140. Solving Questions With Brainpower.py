"""
You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].

The array describes the questions of an exam, where you have to process the questions in order (i.e., starting from question 0) and make a decision whether to solve or skip each question. Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri questions. If you skip question i, you get to make the decision on the next question.

For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
If instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will be unable to solve questions 2 and 3.
Return the maximum points you can earn for the exam.

 

Example 1:

Input: questions = [[3,2],[4,3],[4,4],[2,5]]
Output: 5
Explanation: The maximum points can be earned by solving questions 0 and 3.
- Solve question 0: Earn 3 points, will be unable to solve the next 2 questions
- Unable to solve questions 1 and 2
- Solve question 3: Earn 2 points
Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.
"""
from typing import List
class Solution:
    # TOP DOWN DP 
    def mostPoints(self, questions: List[List[int]]) -> int:
        """
        - two choices: solve or skip
        - if solve, then we can't solve next brainpower questions 
        - if skip, then we can solve next question
        """

        dp={}

        def dfs(idx):
            if idx >= len(questions):
                return 0

            if idx in dp:
                return dp[idx]

            ponts, brainpower = questions[idx]
            skip = dfs(idx+1)
            take= ponts + dfs(idx+brainpower+1)

            dp[idx]=max(skip,take)

            return dp[idx]
        
        return dfs(0)
    # BOTTOM UP DP
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp=[0]*(len(questions)+1)
        n=len(questions)
        for i in reversed(range(n)):
            points, brainpower = questions[i]
            skip=dp[i+1] if i+1<n else 0
            take=points+dp[i+brainpower+1] if i+brainpower+1<=n else points
            dp[i]=max(skip,take)
        return dp[0]



s=Solution()
print(s.mostPoints([[3,2],[4,3],[4,4],[2,5]])) #5
