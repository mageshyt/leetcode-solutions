"""You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

nums1[i] == nums2[j], and
the line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

Return the maximum number of connecting lines we can draw in this way.

 

Example 1:


Input: nums1 = [1,4,2], nums2 = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2."""


class Solution:
    def maxUncrossedLines(self, nums1, nums2) -> int:
        # Recursion solution (MEMOIZATION)

        # Time: O(2^(m+n))  m = len(nums1) n = len(nums2)

        # Space: O(m+n)

        cache = {}

        def dp(i, j):

            if (i, j) in cache:
                return cache[(i, j)]

            if(i == len(nums1) or j == len(nums2)):
                return 0

            if(nums1[i] == nums2[j]):
                cache[(i, j)] = 1 + dp(i+1, j+1)
                return cache[(i, j)]

            else:
                cache[(i, j)] = max(dp(i+1, j), dp(i, j+1))
                return cache[(i, j)]

        return dp(0, 0)


if __name__ == "__main__":
    nums1 = [1, 4, 2, 2]
    nums2 = [1, 2, 2, 4]
    print(Solution().maxUncrossedLines(nums1, nums2))
