"""
You are given a 0-indexed 2D integer array pairs where pairs[i] = [starti, endi]. An arrangement of pairs is valid if for every index i where 1 <= i < pairs.length, we have endi-1 == starti.

Return any valid arrangement of pairs.

Note: The inputs will be generated such that there exists a valid arrangement of pairs.
"""
from typing import List
from collections import defaultdict, Counter
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        degree = Counter()

        for u,v in pairs:
            graph[u].append(v)
            degree[u] += 1
            degree[v] -= 1

        for start in graph:
            if degree[start] == 1:
                break

        res = []

        def dfs(node):
            while graph[node]:
                next_node = graph[node].pop()
                dfs(next_node)
                res.append([node,next_node])

        dfs(start)

        return res[::-1]

