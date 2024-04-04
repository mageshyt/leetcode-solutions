class Solution:
    def maxDepth(self, s: str) -> int:
        count=0 # count of bracket depth
        max_count=0
        for char in s:
            if char=="(":
                count+=1
                max_count=max(max_count,count)
            elif char ==")":
                count-=1
        return max_count