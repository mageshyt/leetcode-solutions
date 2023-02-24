"""ou are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:

If the element is even, divide it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
If the element is odd, multiply it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.

 

Example 1:

Input: nums = [1,2,3,4]
Output: 1
Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.
Example 2:

Input: nums = [4,1,5,20,3]
Output: 3
Explanation: You can transform the array after two operations to [4,2,5,5,3], then the deviation will be 5 - 2 = 3.
Example 3:

Input: nums = [2,10,8]
Output: 3
"""


from sortedcontainers import SortedList
import heapq


class Solution:
    def minimumDeviation(self, nums) -> int:
        minHeap, heapMax = [], -float('inf')

    # O(n log m)
        for num in nums:
            temp = num
            while num % 2 == 0:
                num //= 2

            # for hard num we do num*2
            heapq.heappush(minHeap, (num, max(num*2, temp)))

            heapMax = max(heapMax, num)

            # 2 ->1
            # 4 -> 2 ->1

        # o(n logm * log n)
        res = float('inf')
        heapq.heapify(minHeap)

        while len(minHeap) == len(nums):
            num, maxNum = heapq.heappop(minHeap)
            # update res
            res = min(res, heapMax - num)

            # everytime we pop the value we have to push
            if num < maxNum:
                heapq.heappush(minHeap, (num*2, maxNum))

                heapMax = max(heapMax, num*2)

        return res


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(Solution().minimumDeviation(nums))


# solution 2


def minDeviation(nums) -> int:

    sorted_list = SortedList([])

    for num in nums:
        # if num is even then add it to the list
        if num % 2 == 0:
            sorted_list.add(num)
        else:
            # if num is odd then add num*2 to the list
            sorted_list.add(num*2)

    # run the loop until we cant divide the number by 2
    res = float('inf')
    while True:
        min_val = sorted_list[0]
        max_val = sorted_list[-1]

        diff = max_val - min_val

        res = min(res, diff)  # update the res

        # if the max val is even we can further divide by 2

        if max_val % 2 == 0:
            # remove the max val
            sorted_list.remove(max_val)
            # add the max val/2
            sorted_list.add(max_val//2)

        else:
            return res


nums = [1, 2, 3, 4]
print(minDeviation(nums))
