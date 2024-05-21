class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return self.helper(nums, 0, 0)  # nums, level, current XOR

    def helper(self, nums: List[int], level: int, currentXOR: int) -> int:
        # base condition
        if level == len(nums):
            return currentXOR

        # we have two choices for each element, either include it or exclude it
        # if we include it, we will XOR it with the currentXOR
        _include=self.helper(nums,level+1,currentXOR^nums[level])
        # if we exclude it, we will not XOR it with the currentXOR
        _exclude=self.helper(nums,level+1,currentXOR)

        return _include+_exclude
