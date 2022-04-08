'''Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"'''
\

class Solution:
    def reverseVowels(self, s) -> str:
        vowels=['a','e','i','o','u','A','E','I','O','U']
        s=list(s)
        left=0;
        right=len(s)-1
        while left<right:
            left_char=s[left]
            right_char=s[right]
            if left_char in vowels and right_char in vowels:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
            elif left_char in vowels:
                right-=1
            elif right_char in vowels:
                left+=1
            else:
                left+=1
                right-=1

        return ''.join(s)

test=Solution()
print(test.reverseVowels("hello"))
        
        