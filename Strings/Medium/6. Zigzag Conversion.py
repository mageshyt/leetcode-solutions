class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # edge case
        if numRows == 1:
            return s

        # create a list of strings
        res = [''] * numRows

        row = 0  # current row is always 0
        step = 1  # step is always 1

        for c in s:
            res[row] += c  # add the character to the current row

            if row == 0:
                # if the current row is 0, then we need to go down
                step = 1

            elif row == numRows - 1:
                # if the current row is the last row, then we need to go up
                step = -1

            row += step  # update the current row

        return ''.join(res)


if __name__ == '__main__':
    s = Solution()
    print(s.convert('PAYPALISHIRING', 3))
    print(s.convert('PAYPALISHIRING', 4))
    print(s.convert('A', 1))
