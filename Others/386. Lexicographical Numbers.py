"""
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

 

Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]

"""
from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res=[]

        def dfs(k):

            if k>n:
                return

            res.append(k)

            for i in range(10):
                dfs(k*10+i)

        for i in range(1,10):
            dfs(i)
        return res

if __name__ == "__main__":

    print("TESTING LEXICOGRAPHICAL ORDER")
    s=Solution()
    print(s.lexicalOrder(13)) # [1,10,11,12,13,2,3,4,5,6,7,8,9]
    print("====================================")



