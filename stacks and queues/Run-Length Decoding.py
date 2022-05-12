'''Given a string s, consisting of digits and lowercase alphabet characters, that's a run-length encoded string, return its decoded version.

Note: The original string is guaranteed not to have numbers in it.

Constraints

0 ≤ n ≤ 100,000 where n is the length of s
Example 1
Input
s = "4a3b2c1d2a"
Output
"aaaabbbccdaa"'''

class Solution:
    def solve(self, s):
        stack=[]
        for i,char in enumerate(s):
            if char.isdigit():
                num=char
                while i+1<len(s) and s[i+1].isdigit():
                    num+=s[i+1]
                    i+=1
                print(num)
                if int(num )>0:
                    stack.append(num)
            else:
                stack.append(char*int(stack.pop()))
        return ''.join(stack)

if __name__ == '__main__':
    s = "10a200c"
    print(Solution().solve(s))