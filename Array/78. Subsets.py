
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        self.helper(nums,0,[],result)
        return result

    def helper(self,nums:List[int],index:int,path:List[int],result:List[List[int]]) -> None:
        # base condition to add the path to the result
        result.append(path.copy())

        for i in range(index,len(nums)):
            path.append(nums[i])
            # recursively call the helper function with the updated path and index
            self.helper(nums,i+1,path,result)
            path.pop()


# Time complexity: O(2^n)
# Space complexity: O(2^n)
#
print(Solution().subsets([1,2,3])) # [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]
