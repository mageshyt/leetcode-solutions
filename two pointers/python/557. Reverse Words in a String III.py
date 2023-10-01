class Solution:
    def reverseWords(self, s: str) -> str:

        s=list(s)

        left=0
        right=0

        while right<len(s):
            # find right
            while right<len(s) and s[right]!=' ':
                right+=1

            # reverse
            s[left:right]=self.reverse(s[left:right])

            # move left and right
            left=right+1
            right=left

        return ''.join(s)
        
    def reverse(self, s: str) -> str:
        left=0
        right=len(s)-1

        while left<right:
            # swap
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        
        return s



if __name__ == "__main__":

    print(Solution().reverseWords("Let's take LeetCode contest")) # "s'teL ekat edoCteeL tsetnoc"
