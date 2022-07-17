"""There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

 

Example 1:


Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
Example 2:


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
Example 3:


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500."""


import re


class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, distance: int, k: int) -> int:
        prices=[float('inf')] * n

        prices[src]=0 # we are setting the source city to 0 since we are starting from there

        for i in range(k+1):
            new_prices=prices.copy()

            for src,dst,price in flights:
                if prices[src]==float('inf'): continue

                if prices[src] + price < new_prices[dst]:
                    new_prices[dst]=prices[src] + price

            prices=new_prices
        print(dst )
        return -1 if prices[distance] == float ("inf") else prices[distance]

if __name__ == '__main__':
    s = Solution()
    print(s.findCheapestPrice(n=3, flights = [[0,1,2],[1,2,1],[2,0,10]], src = 1, distance = 2, k = 1))


