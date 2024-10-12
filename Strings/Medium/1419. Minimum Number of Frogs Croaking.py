"""
You are given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so multiple "croak" are mixed.

Return the minimum number of different frogs to finish all the croaks in the given string.

A valid "croak" means a frog is printing five letters 'c', 'r', 'o', 'a', and 'k' sequentially. The frogs have to print all five letters to finish a croak. If the given string is not a combination of a valid "croak" return -1.

 

Example 1:

Input: croakOfFrogs = "croakcroak"
Output: 1 
Explanation: One frog yelling "croak" twice.
Example 2:

Input: croakOfFrogs = "crcoakroak"
Output: 2 
Explanation: The minimum number of frogs is two. 
The first frog could yell "crcoakroak".
The second frog could yell later "crcoakroak".
Example 3:

Input: croakOfFrogs = "croakcrook"
Output: -1
Explanation: The given string is an invalid combination of "croak" from different frogs.
"""

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        if len(croakOfFrogs)%5!=0:
            return -1
        res, count = 0, 0
        c=r=o=a=k=0

        for d in croakOfFrogs:
            if d=='c':
                c+=1
                count+=1

            elif d=='r':
                r+=1
            
            elif d=='o':
                o+=1
            elif d=='a':
                a+=1

            elif d=='k':
                k+=1
                count-=1

            res=max(res,count)

            if c<r or r<o or o<a or a<k:
                return -1
        
        if count==0 and c==r and r==o and o==a and a==k:
            return res

        return -1

print(Solution().minNumberOfFrogs("croakcroak")) #1
print(Solution().minNumberOfFrogs("crcoakroak")) #2

