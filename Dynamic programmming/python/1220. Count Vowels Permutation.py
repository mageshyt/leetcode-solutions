"""Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
Example 3: 

Input: n = 5
Output: 68
 

Constraints:"""

class Solution:
    # DP solution
    def countVowelPermutation(self, n: int) -> int:

        # we will see in reverse way
        """
        'a' -> followed by 'e'
        'e' -> followed by 'a','i'
        'i' -> followed by 'e','o'
        'o' -> followed by 'i' or 'u
        'u' -> followed by 'a'
        """

        prevA = prevE = prevI = prevO = prevU = 1

        for _ in range(1,n):
            curA = prevE
            curE = prevA + prevI
            curI = prevA + prevE + prevO + prevU
            curO = prevI + prevU
            curU = prevA

            prevA,prevE,prevI,prevO,prevU = curA,curE,curI,curO,curU

        return (prevA + prevE + prevI + prevO + prevU)%(10**9+7)
    


    
    # Iterative solution


if __name__ == "__main__":
    n = 2
    print(Solution().countVowelPermutation(n))
        