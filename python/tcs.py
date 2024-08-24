""""
Find the total number of possible increasing
subsequences such that the bitwise AND of
all the elements in the subsequence is 0.
Since the answer can be very large, return it
modulo 109+7.

"""

def count_increasing_subsequences_with_bitwise_and_zero(arr):
    MOD = 10**9 + 7
    n = len(arr)

    # Initialize dp dictionary
    dp = [{} for _ in range(n)]

    for i in range(n):
        dp[i][arr[i]] = 1

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                for mask in list(dp[i].keys()):
                    new_mask = mask & arr[j]
                    if new_mask in dp[j]:
                        dp[j][new_mask] = (dp[j][new_mask] + dp[i][mask]) % MOD
                    else:
                        dp[j][new_mask] = dp[i][mask] % MOD

    # Sum up the counts of subsequences where the AND is zero
    result = 0
    for i in range(n):
        if 0 in dp[i]:
            result = (result + dp[i][0]) % MOD

    return result


arr = [0,1]
# print(count_increasing_subsequences_with_bitwise_and_zero(arr))

# Test cases

"""
You are now at the beginning of A(index 1) and
vou have to go to index N. You can perform the
following moves:
1. Move from the current positioni) to the
next position(i + 1) with cost 1.
2. Move from the current positioni) to any
position ji > i) such that Aj is multiple of
Ai, with cost Aj, and Aj will increase by
one.
For example, let A = [2,7, 9, 11,4], here if you
move from index 1 to index 5 using the second
operation, A will become [2, 7, 9, 11,5] and
the cost is 2.
"""

def min_cost_to_reach_end(arr):
    n = len(arr)
    cache={}

    multiple=lambda x,y: x%y==0 or y%x==0

    def dfs(i,val):
        # base case
        if i==n-1:
            return 0

        if (i,val) in cache:
            return cache[(i,val)]

        # option 1: move to next position
        new_val=arr[i+1]
        res=dfs(i+1,new_val)+1


        # option 2: move to any position j>i such that A[j] is multiple of A[i]
        for j in range(i+1,n):
            if multiple(val,arr[j]):
                # val will be increased by arr[j]
                new_val=arr[j]+1

                res=min(res,dfs(j,new_val)+val)

        cache[(i,val)]=res

        return res

    return dfs(0,arr[0])


# Example usage
A = [2, 4,7,11,13,17,19,23,27,25]
result = min_cost_to_reach_end(A)
print(f"Minimum cost to reach the end: {result}")
print(f"Final array A: {A}")