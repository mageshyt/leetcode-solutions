"""
You are given an integer n indicating there are n specialty retail stores. There are m product types of varying amounts, which are given as a 0-indexed integer array quantities, where quantities[i] represents the number of products of the ith product type.

You need to distribute all products to the retail stores following these rules:

A store can only be given at most one product type but can be given any amount of it.
After distribution, each store will have been given some number of products (possibly 0). Let x represent the maximum number of products given to any store. You want x to be as small as possible, i.e., you want to minimize the maximum number of products that are given to any store.
Return the minimum possible x.
"""
from typing import List
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left = 1
        right = max(quantities)

        while left <= right:
            x = (left + right) // 2

            if self.canDistribute(quantities, x, n):
                right = x - 1
            else:
                left = x + 1

        return left


    def canDistribute(self, quantities, x, n):
        count = 0
        for quantity in quantities:
            count += quantity // x
            if quantity % x != 0:
                count += 1

        return count <= n



if __name__ == "__main__":
    s= Solution()
    n = 3
    quantities = [2, 5, 4]
    print(s.minimizedMaximum(n, quantities))

