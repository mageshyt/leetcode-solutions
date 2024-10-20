from typing import List
class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]
    
    def dfs(self, x: int, children: List[List[int]], s: str) -> None:
        for y in sorted(children[x]):  
            self.dfs(y, children, s)
        self.dfsStr += s[x]  
    
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n = len(parent)
        
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        
        answer = [False] * n
        
        for i in range(n):
            self.dfsStr = ""  
            self.dfs(i, children, s)
            
            if self.isPalindrome(self.dfsStr):
                answer[i] = True
        

        return answer



