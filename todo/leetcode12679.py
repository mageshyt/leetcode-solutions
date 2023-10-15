class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10**9 + 7

        # Ensure arrLen doesn't exceed steps, as the array cannot be longer than the number of steps
        arrLen = min(steps, arrLen)

        # Initialize (DP) array to store the number of ways to reach each position
        dp = [0] * arrLen

        # The initial DP value for position 0 is 1, as there's one way to be at position 0 (starting point)
        dp[0] = 1

        # Iterate through the number of steps
        for s in range(1, steps + 1):
            # Create a new DP array to compute the next steps based on the previous DP array
            next_dp = [0] * arrLen

            # Iterate through each position
            for i in range(arrLen):
                next_dp[i] = dp[i]  # Initialize with the previous value

                # Update the value based on the two possible previous positions
                if i > 0:
                    next_dp[i] = (next_dp[i] + dp[i - 1]) % mod

                if i < arrLen - 1:
                    next_dp[i] = (next_dp[i] + dp[i + 1]) % mod

            # Update the DP array for the next step
            dp = next_dp

        return dp[0]  # Return the number of ways to reach position 0 after the specified steps
