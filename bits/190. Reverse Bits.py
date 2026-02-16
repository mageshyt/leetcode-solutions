class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for _ in range(32):
            lbs = n & 1 # find the lsb
            res = (res << 1) | lbs # shift left and add the lsb
            n >>= 1 # shift right to process the next bit

        return res

if __name__ == "__main__":
    n = 43261596
    print(Solution().reverseBits(n)) # Output: 964176192
        


