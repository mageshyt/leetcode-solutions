class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq=Counter(arr)

        maxLucky=float('-inf')

        for key,val in freq.items():
            if key ==val:
                maxLucky=max(maxLucky,key)
        
        return maxLucky if maxLucky !=float("-inf") else -1
