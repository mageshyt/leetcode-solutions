class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left=0

        res=""


        max_len=max(len(word1),len(word2))


        while left<max_len:

            if left<len(word1):
                res+=word1[left]
            if left<len(word2):
                res+=word2[left]

            left+=1


        return res



if __name__ == '__main__':
    print(Solution().mergeAlternately("abc","pqr"))
    print(Solution().mergeAlternately("ab","pqrs"))
    print(Solution().mergeAlternately("abcd","pq"))
    print(Solution().mergeAlternately("","pqrs"))