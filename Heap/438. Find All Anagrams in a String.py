
'''Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed
 by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''




import collections


class Solution:
    def findAnagrams(self, s: str, p: str) :
        if len(s) < len(p):return []
        p_counter=collections.Counter(p) # this is help to store the count of each char in p
        s_counter=collections.Counter(s[0: len(p)]) # this is help to store the count of each char in s
        result = []
        if s_counter == p_counter:
            result.append(0)
        windowStart=0
        for window_end in range(len(p), len(s)):
            curr=s[window_end]
            s_counter[curr]=s_counter.get(curr,0)+1
            s_counter[s[windowStart]]-=1
            # if it 0, remove it from the counter
            if s_counter[s[windowStart]]==0:
                s_counter.pop(s[windowStart])
            # move the window
            windowStart+=1
            # if the window is equal to the p, we have a match
            if s_counter == p_counter:
                result.append(windowStart)



        return result



                

if __name__ == '__main__':
    s=Solution()
    print(s.findAnagrams("cbaebabacd", "abc"))
    print(s.findAnagrams("abab", "ab"))
    print(s.findAnagrams("magsuresagmsur", "mag"))