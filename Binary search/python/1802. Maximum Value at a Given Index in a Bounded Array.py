class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        right_empty = n - index - 1  # empty space on the right side of the array
        left_empty = index  # empty space on the left side of the array

        height = maxSum
        left = 1
        res=0

        while left <= height:
            mid=(left+height)//2  

            left_sum=0
            right_sum=0
            el=mid-1

            if right_empty < el:
                right_sum = (el*(el+1))//2 - (el-right_empty)*(el-right_empty+1)//2

            else:
                right_sum = (el*(el+1))//2 + right_empty - el

            if left_empty < el:
                left_sum = (el*(el+1))//2 - (el-left_empty)*(el-left_empty+1)//2
            else:
                left_sum = (el*(el+1))//2 + left_empty - el

            sum=left_sum+right_sum+mid

            if sum <= maxSum:
                res=mid
                left=mid+1

            else:
                height=mid-1

        return res