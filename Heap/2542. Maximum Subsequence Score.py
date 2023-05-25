"""
Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
Output: 12
Explanation: 
The four possible subsequence scores are:
- We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
- We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6. 
- We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12. 
- We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
Therefore, we return the max score, which is 12.
"""
import heapq


class Solution:
    def maxScore(self, nums1, nums2, k):

        pair = zip(nums1, nums2)

        # sort the pair by the num2
        sorted_pair = sorted(pair, key=lambda x: - x[1])

        # get the max score
        total = max_score = 0


        heap = []

        for pair in sorted_pair:
            nums1, nums2 = pair  # unpack the pair

            # if the heap is not full, push the nums1 into the heap
            heapq.heappush(heap, nums1)
            total += nums1
            # if the heap is full, pop the smallest element and push the nums1 into the heap
            if len(heap) > k:
                total -= heapq.heappop(heap)

            if(len(heap) == k):
                max_score = max(max_score, total * nums2)

        return max_score


if __name__ == "__main__":
    nums1 = [1, 3, 3, 2]
    nums2 = [2, 1, 3, 4]
    k = 3
    print(Solution().maxScore(nums1, nums2, k))
