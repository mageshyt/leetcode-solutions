"""
A string is beautiful if it's possible to partition it into one or more substrings such that:

Each substring has an even length.
Each substring contains only 1's or only 0's.
You can change any character in s to 0 or 1.

Return the minimum number of changes required to make the string s beautiful.


"""
class Solution:
    def minChanges(self, s: str) -> int:
        changes=0
        start=0
        while start<len(s)-1:
            if s[start] != s[start+1]:
                changes+=1
            start+=2

        return changes

# Time: O(n)
# Space: O(1)

print(Solution().minChanges("0100"))
print(Solution().minChanges("0000"))
print(Solution().minChanges("11000111"))





