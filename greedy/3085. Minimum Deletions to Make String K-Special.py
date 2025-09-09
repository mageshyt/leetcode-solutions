from collections import Counter
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:

        freq = Counter(word)
        counts = sorted(freq.values())

        n = len(counts)
        ans = float('inf')

        for i in range(n):
            range_limit = counts[i] + k
            total = counts[i]

            for j in range(i + 1, n):
                if counts[j] > range_limit:
                    total += range_limit
                else:
                    total += counts[j]

            remain = len(word) - total
            ans = min(ans, remain)

        return ans
