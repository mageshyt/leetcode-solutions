class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [0] * n
        ugly_numbers[0] = 1  # The first ugly number is 1

        # Three pointers for the multiples of 2, 3, and 5
        index_multiple_of_2, index_multiple_of_3, index_multiple_of_5 = 0, 0, 0
        next_multiple_of_2, next_multiple_of_3, next_multiple_of_5 = 2, 3, 5

        for i in range(1, n):
            # Find the next ugly number as the minimum of the next multiples
            next_ugly_number = min(
                next_multiple_of_2, next_multiple_of_3, next_multiple_of_5
            )
            ugly_numbers[i] = next_ugly_number  # Update the ugly number list

            if next_ugly_number == next_multiple_of_2:
                index_multiple_of_2 += 1
                next_multiple_of_2 = ugly_numbers[index_multiple_of_2] * 2
            if next_ugly_number == next_multiple_of_3:
                index_multiple_of_3 += 1
                next_multiple_of_3 = ugly_numbers[index_multiple_of_3] * 3
            if next_ugly_number == next_multiple_of_5:
                index_multiple_of_5 += 1
                next_multiple_of_5 = ugly_numbers[index_multiple_of_5] * 5

        return ugly_numbers[n - 1]  # Return the nth ugly number

# Time complexity: O(n)
# Space complexity O(n)


print(Solution().nthUglyNumber(10))  # 12
print(Solution().nthUglyNumber(1))  # 1
print(Solution().nthUglyNumber(11))  # 15
