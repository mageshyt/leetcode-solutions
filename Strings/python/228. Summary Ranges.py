'''You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"'''


from unittest import TestCase


class Solution:
    def summaryRanges(self, nums) :
        # Edge case
        if not nums:
            return []
        # Initialize Result
        result = []
        start = nums[0]
        end = nums[0]
        for i in range(1, len(nums)):
            print(i,nums[i],start,end)
            # if current number is consecutive to previous number then end = current number
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end:
                    result.append(str(start)) # if we don't find any consecutive numbers then append the start number to result
                else:
                    result.append(str(start) + '->' + str(end))
                
                start = nums[i]
                end = nums[i]
        # if start and end are equal  then we will push start in result
        if start == end:
            result.append(str(start))
        else:
            result.append(str(start) + '->' + str(end))
        return result



TestCase1 = Solution()
res=TestCase1.summaryRanges([0,1,2,4,5,7])
print(res)