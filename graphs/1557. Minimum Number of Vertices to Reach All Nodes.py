import collections


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges):
        # build graph
        adj = collections.defaultdict(list)

        for src, dst in edges:
            adj[dst].append(src)


        # find the nodes with no incoming edges

        res = []

        for node in range(n):
            if not adj[node]:
                res.append(node)

        return res


"""Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
Output: [0,2,3]"""

if __name__ == '__main__':
    n = 5
    edges = [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]
    print(Solution().findSmallestSetOfVertices(n, edges))
