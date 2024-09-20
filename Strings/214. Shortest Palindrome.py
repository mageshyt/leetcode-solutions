"""You are given a string s. You can convert s to a 
palindrome by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

 

Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: s = "abcd"
Output: "dcbabcd"
"""
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n=len(s)
        if n<=1:
            return s
        l,r=0,n-1

        while r>=0:
            # find the longest palindrome from the start
            if s[l] == s[r]:
                print(f"MOVING ({l},{r}), ",s[l],s[r])
                l+=1
            r-=1

        if l==n:
            return s

        suffix=s[l:]
        prefix=s[:l]
        print("[PRFIX,SUFFIX]",prefix,suffix)

        return suffix[::-1]+self.shortestPalindrome(prefix)+suffix 



print("TESTING THE SHORTEST PALINDROME")
s=Solution()
print(s.shortestPalindrome("aacecaaa")) # "aaacecaaa"
print("====================================")
print(s.shortestPalindrome("abcd")) # "dcbabcd"
print("END OF TESTING")
