"""You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters. You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost of changing the character original[i] to the character changed[i].

You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.

Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.

Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].



Example 1:

Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
Output: 28
Explanation: To convert the string "abcd" to string "acbe":
- Change value at index 1 from 'b' to 'c' at a cost of 5.
- Change value at index 2 from 'c' to 'e' at a cost of 1.
- Change value at index 2 from 'e' to 'b' at a cost of 2.
- Change value at index 3 from 'd' to 'e' at a cost of 20.
The total cost incurred is 5 + 1 + 2 + 20 = 28.
It can be shown that this is the minimum possible cost.
Example 2:

Input: source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2]
Output: 12
Explanation: To change the character 'a' to 'b' change the character 'a' to 'c' at a cost of 1, followed by changing the character 'c' to 'b' at a cost of 2, for a total cost of 1 + 2 = 3. To change all occurrences of 'a' to 'b', a total cost of 3 * 4 = 12 is incurred.
Example 3:

Input: source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000]
Output: -1
Explanation: It is impossible to convert source to target because the value at index 3 cannot be changed from 'd' to 'e'.
 """

from typing import List
from collections import defaultdict
import heapq
class Solution:
    # Time complexity: O(n+m) | Space complexity: O(n)
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        adj=defaultdict(list) # [src,dst,cost]

        for src,dst,cur_cost in zip(original,changed,cost):
            adj[src].append((dst,cur_cost))


        n=len(source)
        # implement dijkstra algorithm

        def  dijkstra(src):
            heap=[(0,src)]

            min_cost_map=defaultdict(lambda: float("inf"))


            while heap:
                cur_cost,cur_node=heapq.heappop(heap)

                if cur_node in min_cost_map:
                    continue

                min_cost_map[cur_node]=cur_cost

                for neighbor,neighbor_cost in adj[cur_node]:
                    heapq.heappush(heap,(cur_cost+neighbor_cost,neighbor))


            return min_cost_map



        min_cost_map={c:dijkstra(c) for c in set(source)}
        min_cost= 0
        for src,dst in zip(source,target):
            # if destination is not in the min_cost_map of source, it means it is impossible to convert source to target
            if dst not in min_cost_map[src]:
                return -1

            min_cost+=min_cost_map[src][dst]

        return min_cost




print(Solution().minimumCost("abcd", "acbe", ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20]))  # 28
