
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # base cases
        if not s or not t:
            return ""
        if len(s) < len(t):
            return ""
        
        # create a dictionary of the characters in t
        t_dict = Counter(t)

        window= {}

        have, need = 0, len(t_dict)

        res,resLen=[-1,-1], float('inf') # [start, end]

        left=0

        for right in range(len(s)):
            curr=s[right]
            window[curr]=window.get(curr,0)+1

            if curr in t_dict and window[curr]==t_dict[curr]:
                have+=1

            while have==need:
                curr_size=right-left+1
                # we found the smallest window
                if curr_size<resLen:
                    res=[left,right]
                    resLen=curr_size
                # move the left pointer
                window[s[left]]-=1
                # if the character is in the dictionary and the window has less than the required amount
                if s[left] in t_dict and window[s[left]]<t_dict[s[left]]:
                    have-=1

                left+=1

        if res[0]==-1:
            return ""
        
        return s[res[0]:res[1]+1]
    
# Time complexity: O(n)
# Space complexity: O(1) since the size of the window is fixed and the size of the dictionary is fixed
    


# Test cases
test = Solution()
print(test.minWindow("ADOBECODEBANC", "ABC") )
