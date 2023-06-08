class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:

        # logic go from last bit to first bit
        # if 1 need flip anyone  
        # if 0 need flip both

        float
        while a > 0 or b > 0 or c > 0:
            a_last= a & 1
            b_last = b & 1
            c_last = c & 1

            if c_last == 1:
                if a_last == 0 and b_last == 0:
                    count += 1

            else:
                if a_last == 1:
                    count += 1
                if b_last == 1:
                    count += 1
            # move to next bit
            a = a >> 1

            b = b >> 1

            c = c >> 1

        return count