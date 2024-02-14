from typing import List
from  collections import defaultdict
class Solution:
    # Time: O(nlogn) | Space: O(n)
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums
        
        signedArray = defaultdict(list)

        for num in nums:
            if num < 0:
                signedArray['negative'].append(num)
            else:
                signedArray['positive'].append(num)

        result = []

        for i in range(max(len(signedArray['positive']), len(signedArray['negative']))):
            if i < len(signedArray['positive']):
                result.append(signedArray['positive'][i])
            if i < len(signedArray['negative']):
                result.append(signedArray['negative'][i])

        return result
    
    # Time: O(nlogn) | Space: O(1)







if __name__ == "__main__":
    nums = [3,1,-2,-5,2,-4]
    print(Solution().rearrangeArray(nums)) # [5, 1, 4, 2, 3]
  
        