class Solution:
    def binaryGap(self, n: int) -> int:
        binary_representation = bin(n)[2:]  # Get binary representation of n

        max_one = 0
        curr_count = 0
        found = False

        for bit in binary_representation:
            if bit == '1':
                if found:
                    max_one = max(max_one, curr_count)
                found = True
                curr_count = 0  # Reset count after finding a '1'
            elif found:
                curr_count += 1  # Increment count only if we've found a '1'

        return max_one
