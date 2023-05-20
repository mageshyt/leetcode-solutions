from collections import *


class Solution:
    def calcEquation(self, equations, values, queries):
        adj = defaultdict(list)

        for i, edge in enumerate(equations):
            # a/b and b/a
            [a, b] = edge
            adj[a].append((b, values[i]))
            adj[b].append((a, 1/values[i]))
        print(adj)

        def bfs(src, target):
            # in which case x/x = -1 which mean x is not in out graph
            if src not in adj or target not in adj:
                return -1

            q = deque()
            q.append((src, 1))
            visited = set()

            while q:
                node, weight = q.popleft()

                if node == target:
                    return weight

                for neighbor, edge_weight in adj[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append((neighbor, weight*edge_weight))

            return -1

        return [bfs(src, target) for src, target in queries]


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

print(Solution().calcEquation(equations, values, queries))
