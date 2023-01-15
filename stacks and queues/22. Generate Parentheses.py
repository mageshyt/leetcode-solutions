'''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]'''


class Solution:
    def generateParenthesis(self, n: int):
        # base case when n = 0, return an empty list
        if n == 0:
            return []

        # base case when n = 1, return a list with one element
        if n == 1:
            return ["()"]

        # initialize an empty list to store all the combinations
        combinations = []

        # only add open parentheses if open < n
        # only add close parentheses if close < open

        def backtrack(_open, close, combination):
            # base case when open and close are both equal to n
            if _open == n and close == n:
                combinations.append(combination)
                return

            # only add open parentheses if open < n
            if _open < n:
                backtrack(_open + 1, close, combination + "(")

            # only add close parentheses if close < open
            if close < _open:
                backtrack(_open, close + 1, combination + ")")

        backtrack(0, 0, "")
        return combinations


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))
    print(Solution().generateParenthesis(1))
    print(Solution().generateParenthesis(0))
