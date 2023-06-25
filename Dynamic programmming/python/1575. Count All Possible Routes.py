"""You are given an array of distinct positive integers locations where locations[i] represents the position of city i. You are also given integers start, finish and fuel representing the starting city, ending city, and the initial amount of fuel you have, respectively.

At each step, if you are at city i, you can pick any city j such that j != i and 0 <= j < locations.length and move to city j. Moving from city i to city j reduces the amount of fuel you have by |locations[i] - locations[j]|. Please notice that |x| denotes the absolute value of x.

Notice that fuel cannot become negative at any point in time, and that you are allowed to visit any city more than once (including start and finish).

Return the count of all possible routes from start to finish. Since the answer may be too large, return it modulo 109 + 7."""

from typing import List

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        mod=10**9+7

        memo={}

        def dfs(start,fuel):
            # base case
            if fuel<0:
                return 0
            
            if (start,fuel) in memo:
                return memo[(start,fuel)]
            # recursive case

            ans=0
            
            # if we reach the finish
            if start==finish:
                ans+=1
            
            for nextCity in range(len(locations)):
                # if we are not in the same city and we have enough fuel to go to the next city
                if nextCity!=start:
                    ans+=dfs(nextCity,fuel-abs(locations[nextCity]-locations[start]))


            memo[(start,fuel)]=ans%mod

            return memo[(start,fuel)]
        
        return dfs(start,fuel)
    

# Path: Dynamic programmming/python/1583. Count Unhappy Friends.py

 

locations = [2,3,6,8,4]

start = 1

finish = 3

fuel = 5

s=Solution()

print(s.countRoutes(locations,start,finish,fuel))