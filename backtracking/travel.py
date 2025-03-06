
import math


def travelerCity(n, k):
    res = []

    def backtrack(start, path):
        if start > k:
            return
        if len(path) == n:
            res.append(path[:])
            return

        max_additional = math.floor(
            math.log(k / start, 2)) if start <= k else 0

        if len(path) + max_additional < n:
            return

        for i in range(start*2, k+1):
            path.append(i)
            backtrack(i, path)
            path.pop()
    for i in range(1, k+1):
        backtrack(i, [i])

    return res


def travelerCityCount(n, k):
    res = 0
    dp = {}  # (start, visited) -> count

    def backtrack(start, visited):
        if start > k:
            return 0
        if visited == n:
            return 1

        if (start, visited) in dp:
            return dp[(start, visited)]
        take = 0
        # take
        for i in range(start*2, k+1):
            take += backtrack(i, visited+1)

        dp[(start, visited)] = take

        return dp[(start, visited)]

    return backtrack(1, 1)


if __name__ == "__main__":
    # print(travelerCity(3, 10))
    # print(travelerCity(5, 1000))
    print(travelerCityCount(5, 1000))
