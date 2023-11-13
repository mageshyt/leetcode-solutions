class Solution:
    def sortVowels(self, s: str) -> str:
        position={"A":1,"E":2,"I":3,"O":4,"U":5,"a":6,"e":7,"i":8,"o":9,"u":10}
        sorted_vowels=["" for _ in range(len(position))] 

        result = ["" for _ in range(len(s))]

        for i in range(len(s)):
            if s[i] in position:
                # print(s[i])
                pos=position[s[i]]-1
                sorted_vowels[pos]+=s[i]
            else:
                result[i]= s[i]

        sorted_vowels = "".join(sorted_vowels)
        # print(sorted_vowels, result,s)
        miss_count=0

        for i  in range(len(result)):
            if result[i] == "":
                result[i] = sorted_vowels[miss_count]
                miss_count+=1

        return "".join(result)  
    
    # Big o analysis

    # Time complexity: O(n) where n is the length of the string

    # Space complexity: O(n) where n is the length of the string


print(Solution().sortVowels("uZcPmqAd"))
