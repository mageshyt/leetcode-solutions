'''You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.

 

Example 1:

Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.
Example 2:

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.'''





from typing import Counter


class Solution:
    def deleteAndEarn(self, nums):

        count_val=Counter(nums)
        # after removing the duplicate values
        nums=sorted(list(set(nums)))
        # two keep track of our earns
        earn_one=0 
        earn_two=0
        for i in range(len(nums)):
            current_amount=nums[i]*count_val[nums[i]] # current value * count 
            '''
            ex: nums=[2,2,3,3,3,4]
            here 2 occurs twice, so we can earn 2*2=4 points
            same for 3, 3*3=9 points
            '''
            if i >0 and nums[i]==nums[i-1]+1:
                temp=earn_two
                earn_two=max(current_amount+earn_one,earn_two)
                earn_one=temp
            else:
                temp=earn_two
                earn_two=current_amount+earn_two
                earn_one=temp

        return max(earn_one,earn_two)

test1=Solution()
print(test1.deleteAndEarn([3,4,2]))

            

