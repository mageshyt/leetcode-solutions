"""
Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.

 

Example 1:

Input: n = "123"
Output: "121"
Example 2:

Input: n = "1"
Output: "0"
Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.
"""
class Solution:
    def convert(self, num: int) -> int:
        s = str(num)
        n = len(s)
        l, r = (n - 1) // 2, n // 2 # start and end points
        s_list = list(s)

        while l >= 0:
            s_list[r] = s_list[l]
            r += 1
            l -= 1
        return int("".join(s_list))

    def previous_palindrome(self, num: int) -> int:
        left, right = 0, num
        ans = float("-inf")
        while left <= right:
            mid = (right - left) // 2 + left
            palin = self.convert(mid)
            # if palindrome is less than the number then make it as ans and move the left pointer to maximize the result
            if palin < num:
                ans = palin
                left = mid + 1
            else:
                # move the right to minimize the result 
                right = mid - 1
        return ans

    def next_palindrome(self, num: int) -> int:
        left, right = num, int(1e18)  # left and righ boundary to find next palindrome
        ans = float("-inf")
        while left <= right:
            mid = (right - left) // 2 + left
            palin = self.convert(mid)
            if palin > num:
                ans = palin
                right = mid - 1
            else:
                left = mid + 1
        return ans

    def nearestPalindromic(self, n: str) -> str:
        num = int(n)
        prev_pali = self.previous_palindrome(num)
        next_pali= self.next_palindrome(num)

        if abs(prev_pali - num) <= abs(next_pali - num):
            return str(prev_pali)

        return str(next_pali)
