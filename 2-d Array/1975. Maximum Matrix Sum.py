
from typing import List
class Solution:
    # Time complexity: O(N*M) | Space complexity: O(1)
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neg_count = 0
        abs_sum = 0
        min_abs = float('inf')
        for row in matrix:
            for num in row:
                abs_sum += abs(num)
                if num < 0:
                    neg_count += 1
                min_abs = min(min_abs, abs(num))
        return abs_sum if neg_count % 2 == 0 else abs_sum - 2 * min_abs



