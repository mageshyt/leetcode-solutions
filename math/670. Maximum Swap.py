class Solution:
    def maximumSwap(self, num: int) -> int:
        # conver to list
        nums=list(str(num))

        maxIdx = -1
        swapI, swapJ = -1, -1

        # find the first digit that is smaller than the max digit on its right

        for i in range(len(nums)-1, -1, -1):
            # if current digit is greater than max digit on its right
            if nums[i] > nums[maxIdx]:
                maxIdx = i

            if nums[i] < nums[maxIdx]:
                # if the curr digit is smaller we have to make swap

                swapI, swapJ = i, maxIdx

        # swap the two digits
        nums[swapI], nums[swapJ] = nums[swapJ], nums[swapI]

        return int("".join(nums))



