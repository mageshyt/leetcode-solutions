"""Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice."""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        Check if a given string is formed by repeating a substring multiple times.
        
        Args:
            s (str): Input string to be checked.
        
        Returns:
            bool: True if the string can be formed by repeating a substring, False otherwise.
        """
        n = len(s)  # Length of the input string
        
        # Iterate through possible substring lengths from 1 to n//2
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                # Get the potential substring
                sub_string = s[:i]
                
                # Check if repeating the substring n//i times results in the original string
                if (sub_string * (n // i)) == s:
                    return True
        
        return False



s=Solution()
print(s.repeatedSubstringPattern("abab"))
