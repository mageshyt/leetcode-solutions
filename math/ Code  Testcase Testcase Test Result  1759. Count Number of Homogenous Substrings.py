class Solution:
    def countHomogenous(self, s: str) -> int:
        
        left = 0

        right = 0

        cache={}

        while right < len(s):
            
            if s[left] == s[right]:
                
                right += 1

                # get the substring from left to right
                # and add it to the cache

                substr = s[left:right]

                # get all possible substrings from left to right

                for i in range(left, right):

                    substr = s[left:i+1]

                    cache[substr] = cache.get(substr, 0) + 1


            else:
                left += 1


        return sum(cache.values()) % (10**9 + 7)
    
    # optimized solution

    def countHomogenous(self, s: str) -> int:

        count = 0
        curr_homogenous = 0

        MOD=10**9 + 7

        for  i in range(len(s)):

            if s[i] != s[i-1] or i == 0:

                curr_homogenous = 1
            else:
                curr_homogenous += 1

            count =(count + curr_homogenous) % MOD


        return count 

    

if __name__ == '__main__':
    s = Solution()
    print(s.countHomogenous("abbcccaa"))