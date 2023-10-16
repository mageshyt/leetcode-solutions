from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # base case

        if rowIndex == 0:
            return [1]

        if rowIndex == 1:

            return [1, 1]

        # recursive case
        def helper(row):
            if row == 1:
                return [1, 1]
            else:
                prev_row = helper(row-1)
                new_row = [1]
                for i in range(1, len(prev_row)):
                    # now we add the previous row's elements
                    new_row.append(prev_row[i-1]+prev_row[i])

                new_row.append(1)
                return new_row

        return helper(rowIndex)


if __name__ == "__main__":
    s = Solution()
    print(s.getRow(10))
