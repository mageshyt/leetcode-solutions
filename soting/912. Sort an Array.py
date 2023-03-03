class Solution:
    def sortArray(self, nums):
        if(len(nums) <= 1):
            return nums

        mid = len(nums)//2

        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)

    def merge(self, left_arr, right_arr):
        print(left_arr, right_arr)
        res = []

        p1 = 0
        p2 = 0

        while (p1 < len(left_arr) and p2 < len(right_arr)):

            if left_arr[p1] > right_arr[p2]:
                res.append(right_arr[p2])
                p2 += 1

            else:
                res.append(left_arr[p1])

                p1 += 1

        while p2 < len(right_arr):
            res.append(right_arr[p2])
            p2 += 1

        while p1 < len(left_arr):
            res.append(left_arr[p1])
            p1 += 1

        return res


if __name__ == "__main__":
    print(Solution().sortArray([9, 45, 12, 1, 8]))
