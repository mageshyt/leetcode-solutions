class Solution(object):
    def wordSubsets(self, word1, word2):
        def helper(word):
            res=[0]*26
            for c in word:
                 res[ord(c)-ord('a')]+=1
            return res
        
        b_max=helper(word2[0])

        for word in word2:
            for i,char in enumerate(helper(word)):
                b_max[i]=max(b_max[i],char)

        res=[]

        for word in word1:
            if all(helper(word)[i]>=b_max[i] for i in range(26)):
                res.append(word)
        return res


if __name__ == "__main__":
    s=Solution()
    print(s.wordSubsets(["amazon","apple","facebook","google","leetcode"],["lo", "eo"]))



