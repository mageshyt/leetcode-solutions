class Solution:
    def minimumDeletions(self, s: str) -> int:
        res=0

        # count the number of 'b' in the string
        count=0

        for char in s:
            if char=='b':
                count+=1
            elif count >0 :
                count-=1
                res+=1

        return res


        # count the number of 'a' in the string




# Time complexity: O(N)
# Space complexity: O(N)
print(Solution().minimumDeletions("aababbab")) # 2