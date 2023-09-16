class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        mod = 10**9 + 7

        # Create a 2D DP array to store the number of ways to create playlists of length 'i'
        # using 'j' distinct songs.
        dp = [[0 for _ in range(n + 1)] for _ in range(goal + 1)]

        # Base case: there's only one way to create an empty playlist of length 0 using 0 songs.
        dp[0][0] = 1

        for i in range(1, goal + 1):
            for j in range(1, min(i, n) + 1):
                # Calculate the number of ways to add the 'j'-th distinct song to the playlist of length 'i'.
                dp[i][j] = dp[i-1][j-1] * (n - j + 1) % mod

                # If 'j' is greater than 'k', we can add any song from the 'j-k' distinct songs already present
                # in the playlist of length 'i-1'. So, we add 'dp[i-1][j] * (j-k)' to the total number of ways.
                if j > k:
                    dp[i][j] = (dp[i][j] + dp[i-1][j] * (j - k)) % mod

        # The total number of ways to create a playlist of length 'goal' using 'n' distinct songs is stored in dp[goal][n].
        return dp[goal][n]
