class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        difference = []

        if len(s) != len(goal):
            return False
        
        if s == goal:

            return False if len(set(s)) == len(s) else True

        for i in range(len(s)):

            if s[i] != goal[i]:
                difference.append(i)


        if len(difference) != 2:
            return False
        
        if s[difference[0]] == goal[difference[1]] and s[difference[1]] == goal[difference[0]]:

            return True
        


        return False
    
s = "ab"
goal = "ba"

print(Solution().buddyStrings(s, goal))