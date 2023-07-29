"""There are two types of soup: type A and type B. Initially, we have n ml of each type of soup. There are four kinds of operations:

Serve 100 ml of soup A and 0 ml of soup B,
Serve 75 ml of soup A and 25 ml of soup B,
Serve 50 ml of soup A and 50 ml of soup B, and
Serve 25 ml of soup A and 75 ml of soup B.
When we serve some soup, we give it to someone, and we no longer have it. Each turn, we will choose from the four operations with an equal probability 0.25. If the remaining volume of soup is not enough to complete the operation, we will serve as much as possible. We stop once we no longer have some quantity of both types of soup.

Note that we do not have an operation where all 100 ml's of soup B are used first.

Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same time. Answers within 10-5 of the actual answer will be accepted.

Example 1:

Input: n = 50
Output: 0.62500
Explanation: If we choose the first two operations, A will become empty first.
For the third operation, A and B will become empty at the same time.
For the fourth operation, B will become empty first.
So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.
 """
class Solution:
    def __init__(self):
        self.optionA = [100, 75, 50, 25]
        self.optionB = [0, 25, 50, 75]

    def soupServings(self, n):
        dp = {}  # Memoization dictionary to store computed probabilities

        def dfs(a, b):
            # Base case: If both types of soup are empty, return 0.5 (half probability)
            if a == 0 and b == 0:
                return 0.5
                
            # If soup A is empty, return 1 (as soup A is exhausted first)
            if a == 0:
                return 1
            # If soup B is empty, return 0 (as soup B is exhausted first)
            if b == 0:
                return 0

            # If (a, b) combination is already computed, return the result
            if (a, b) in dp:
                return dp[(a, b)]

            ans = 0
            # Calculate the probability for each of the four operations
            for i in range(4):
                remainingA = max(0, a - self.optionA[i])  # Remaining soup A after operation i
                remainingB = max(0, b - self.optionB[i])  # Remaining soup B after operation i
                ans += dfs(remainingA, remainingB) * 0.25  # Add the probability for operation i

            dp[(a, b)] = ans  # Memoize the result for future use
            return dp[(a, b)]

        # If n is very large, return 1.0 as the probability of A being empty first is almost certain
        if n >= 4800:
            return 1.0

        # Otherwise, calculate and return the probability using the dfs function
        return dfs(n, n)

# Test the code with the given input n=50
if __name__ == "__main__":
    n = 50
    print(Solution().soupServings(n))

