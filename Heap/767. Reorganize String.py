"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
"""
from collections import *
from heapq import *

class Solution:
    def reorganizeString(self, s: str) -> str:

        counter=Counter(s)
        print([item for item in counter.items()])
        heap=[[-item[1],item[0]] for item in counter.items()] # [count of char, char]
        heapify(heap)

        res=""

        while heap:
            count,char=heappop(heap)
            # if no res or last char in res is not the same as current char
            if not res or res[-1]!=char:
                # we can add this char to res

                res+=char

                # if count of this char is greater than 1
                if (-count)>1:
                    # we can add this char back to heap with count-1
                    heappush(heap,[count+1,char])
            else:
                # if last char in res is the same as current char
                # we need to find another char
                if not heap:
                    # if heap is empty, we cannot find another char
                    return ""
                
                # find another char
                count2,char2=heappop(heap)
                res+=char2
                if (-count2)>1:
                    heappush(heap,[count2+1,char2])
                # add current char back to heap
                heappush(heap,[count,char])
        return res





if __name__ == '__main__':
    s=Solution()
    print(s.reorganizeString("aab"))
    print(s.reorganizeString("aaab"))
