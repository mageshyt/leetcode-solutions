"""A truck has two fuel tanks. You are given two integers, mainTank representing the fuel present in the main tank in liters and additionalTank representing the fuel present in the additional tank in liters.

The truck has a mileage of 10 km per liter. Whenever 5 liters of fuel get used up in the main tank, if the additional tank has at least 1 liters of fuel, 1 liters of fuel will be transferred from the additional tank to the main tank.

Return the maximum distance which can be traveled.

Note: Injection from the additional tank is not continuous. It happens suddenly and immediately for every 5 liters consumed.
"""


class Solution(object):
    def distanceTraveled(self, mainTank, additionalTank):
        """
        :type mainTank: int
        :type additionalTank: int
        :rtype: int
        """
        if mainTank < 5:
            return mainTank * 10

        if additionalTank < 1:
            return mainTank * 10

        distance = 0
        while mainTank >= 5:
            distance += 50

            mainTank -= 5

            if additionalTank == 1:
                mainTank += 1
                break

            additionalTank -= 1
            if additionalTank < 1:
                break

            mainTank += 1

        return distance + mainTank * 10


mainTank = 5
additionalTank = 1
print(Solution().distanceTraveled(mainTank, additionalTank))


"""You are given a positive integer array nums.

Partition nums into two arrays, nums1 and nums2, such that:

Each element of the array nums belongs to either the array nums1 or the array nums2.
Both arrays are non-empty.
The value of the partition is minimized.
The value of the partition is |max(nums1) - min(nums2)|.

Here, max(nums1) denotes the maximum element of the array nums1, and min(nums2) denotes the minimum element of the array nums2.

Return the integer denoting the value of such partition."""


class Solution(object):
    def findValueOfPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        minDiff = float('inf')

        for i in range(1, len(nums)):
            minDiff = min(minDiff, abs(nums[i] - nums[i - 1]))

        return minDiff


nums = nums = [1, 3, 2, 4]

print(Solution().findValueOfPartition(nums))
