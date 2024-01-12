class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels='aeiouAEIOU'
        n=len(s)
        firstHafl=s[:n//2]
        secondHalf=s[n//2:]

        firstHaflCount=[1 for i in firstHafl if i in vowels]
        secondHalfCount=[1 for i in secondHalf if i in vowels]

        return sum(firstHaflCount)==sum(secondHalfCount)


    

