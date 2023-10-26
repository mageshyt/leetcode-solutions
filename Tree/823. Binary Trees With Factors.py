"""Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.

 

Example 1:

Input: arr = [2,4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]
Example 2:

Input: arr = [2,4,5,10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
"""

from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        dp=[1]*len(arr)

        # sort the array
        arr.sort()

        # create a dictionary to store the index of each element
        index={x:i for i,x in enumerate(arr)}

        # create a dictionary to store the number of trees for each element
        trees={x:1 for x in arr} # x->number of trees
 
        print(index,trees)
        # iterate through the array

        for idx,tree in enumerate(arr):
            for i in range(idx):
                if tree%arr[i]==0:
                    # if the factor is in the array
                    if tree//arr[i] in index:
                        # add the number of trees for the factor to the current tree
                        trees[tree]+=trees[arr[i]]*trees[tree//arr[i]]
                        # print(trees)  

        return sum(trees.values())%(10**9+7)
    
if __name__ == "__main__":
    arr = [2,4,5,10]
    print(Solution().numFactoredBinaryTrees(arr))

        