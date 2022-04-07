class Solution:
    def findAnagrams(self, s: str, p: str)  :
		
        if len(p) > len(s): return [] # edge case if the len of p is greater than len of s we need to return [] because we cant find any anagram from string s if it less then len of p
        p_count={} # this is help to store the count of each char in p
        s_count={} # this is help to store the count of each char in s
        result = []
        for i in range(len(p)):
            # here we are checking wheather it has the char or not if it was there then we will increment the count by 1
            p_count[p[i]]=p_count.get(p[i],0)+1
            s_count[s[i]]=s_count.get(s[i],0)+1
        if p_count==s_count:
            result.append(0)
        left=0
        for right in range(len(p),len(s)):
            current_char=s[right]
            s_count[current_char]=1+s_count.get(current_char,0)
            s_count[s[left]]-=1
            # here we are checking whether the value at left pointer is 0 or not
            if s_count[s[left]] ==0:
                # if it was 0 then we will remove ir
                s_count.pop(s[left])
            # we will increment the left counter
            left+=1
            if s_count==p_count:
                result.append(left)
        return result


        