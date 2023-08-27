from typing import List
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # sort the paris based on the end time
        pairs.sort(key =lambda pair:pair[1])

        length = 1 # minimum length is 1

        # initialize the end time of the first interval
        end = pairs[0][1]

        # loop through the remaining intervals from the second one onwards

        for i in range(1,len(pairs)):
            # if we need to add the current interval to the chain then the pair end should be greater then [end]
            if pairs[i][0] > end:
                # increase the length of the chain
                length += 1
                # update the end time to the current interval's end time
                end = pairs[i][1]

        return length
    def findLongestChain2(self,pairs):
        # TODO: Fix the isue
        cache={}
        # dfs

        def dfs(pairs,prev,end):
            if not pairs:
                return 0
            
            if (prev,end) in cache:
                return cache[(prev,end)]

            taken = 0
            not_taken = 0
            if pairs[0][0] > end:
                taken = 1 + dfs(pairs[1:],pairs[0][1],pairs[0][1])
            not_taken = dfs(pairs[1:],prev,end)

            cache[(prev,end)] = max(taken,not_taken)
            return cache[(prev,end)]
        

        
        return dfs(pairs,None,float('-inf'))
    

pairs = [[1,2],[2,3],[3,4]]
print(Solution().findLongestChain2(pairs))



