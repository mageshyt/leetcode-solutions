def count_ways_to_reach_island(N):
    ways = [0] * (N + 1)
    ways[1] = 1

    for j in range(2, N + 1):
        for i in range(1, j):
            if j % i == 0:  # If i is a divisor of j
                ways[j] += ways[i]  # Add the number of ways to reach i to j

    return ways[N]

def counWays(n):
    memo={}

    def dfs(i):
        # base case
        if i==1:
            return 1
        if i in memo:
            return memo[i]

        result=0

        for j in range(1,i):
            if i%j==0:
                result+= dfs(j)

        memo[i]= result
        return result

    return dfs(n)
import math

def count_ways_to_reach_island2(N):
    # Memoization dictionary to store the number of ways to reach each island
    memo = {}

    # Recursive function to count the number of ways to reach island j
    def ways(j):
        # Base case: There's only 1 way to reach Island 1
        if j == 1:
            return 1
        # If the result is already computed, return it
        if j in memo:
            return memo[j]
        
        # Initialize count of ways to 0
        count = 0
        # Efficiently find divisors of j by iterating up to sqrt(j)
        for i in range(1, int(math.sqrt(j)) + 1):
            if j % i == 0:
                # i is a divisor
                count += ways(i)
                # j // i is also a divisor, avoid double counting when i == j // i
                if i != j // i and j // i != j:
                    count += ways(j // i)
        
        # Store the computed result in memoization dictionary
        memo[j] = count
        return count

    # Call the recursive function starting from N
    return ways(N)

# Reading input
T = int(input())  # Number of test cases
for _ in range(T):
    N = int(input())
    print(count_ways_to_reach_island(N))
    print(counWays(N))
    print(count_ways_to_reach_island2(N))
    print("=========")

# print(count_ways_to_reach_island(4)) # 3
# print(counWays(4)) # 3
# print(count_ways_to_reach_island2(4)) # 3
# print("=====")
# print(count_ways_to_reach_island(23)) # 3
# print(counWays(23)) # 3
# print(count_ways_to_reach_island2(23)) # 3
# print("=====")
# print("=====")
# print(count_ways_to_reach_island(13)) # 3
# print(counWays(13)) # 3
# print(count_ways_to_reach_island2(13)) # 3
# print("=====")
# print("=====")
# print(count_ways_to_reach_island(11)) # 3
# print(counWays(11)) # 3
# print(count_ways_to_reach_island2(11)) # 3
# print("=====")
