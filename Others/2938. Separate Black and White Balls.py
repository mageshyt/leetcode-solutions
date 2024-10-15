class Solution:
    def minimumSteps(self, s: str) -> int:
        total_swaps=0
        white_balls=0

        for i in range(len(s)-1,-1,-1):
            if s[i]=='0':
                white_balls+=1
            else:
                total_swaps+=white_balls


        return total_swaps

print(Solution().minimumSteps("1100")) # r
print(Solution().minimumSteps("101")) # r
