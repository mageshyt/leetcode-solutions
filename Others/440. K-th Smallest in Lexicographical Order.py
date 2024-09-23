class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        def count(start, end, n):
            cnt = 0
            while start <= n:
                cnt += min(n + 1, end) - start
                start *= 10
                end *= 10
            return cnt

        curr = 1
        k -= 1
        while k > 0:
            # curr and its neighbors are in the same subtree
            steps = count(curr, curr + 1, n)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1

        return curr


if __name__ == "__main__":
    print("TESTING K-TH SMALLEST IN LEXICOGRAPHICAL ORDER...")
    s = Solution()
    print(s.findKthNumber(13, 2))  # 10
    print(s.findKthNumber(13, 3))  # 11
    print(s.findKthNumber(13, 4))  # 12
