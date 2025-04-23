
from collections import defaultdict
class Solution:
    def countLargestGroup(self, n: int) -> int:
        counter=defaultdict(int)

        for i in range(1,n+1):
            counter[sum(map(int,str(i)))] += 1

        max_count = max(counter.values())

        print(counter)

        return sum(1 for count in counter.values() if count == max_count)


if __name__ == "__main__":
    n = 13
    print(Solution().countLargestGroup(n))
    # Output: 4
    # Explanation: The groups are:
    # - Group 1: [1, 10] with sum = 1
    # - Group 2: [2, 11] with sum = 2
    # - Group 3: [3, 12] with sum = 3
    # - Group 4: [4, 5, 6, 7, 8, 9, 13] with sum = 4
    # There are four groups with the largest size. So return 4.
