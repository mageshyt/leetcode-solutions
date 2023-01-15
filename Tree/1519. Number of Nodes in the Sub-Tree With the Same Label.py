'''You are given a tree (i.e. a connected, undirected graph that has no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges. The root of the tree is the node 0, and each node of the tree has a label which is a lower-case character given in the string labels (i.e. The node with the number i has the label labels[i]).

The edges array is given on the form edges[i] = [ai, bi], which means there is an edge between nodes ai and bi in the tree.

Return an array of size n where ans[i] is the number of nodes in the subtree of the ith node which have the same label as node i.

A subtree of a tree T is the tree consisting of a node in T and all of its descendant nodes.

 

Example 1:


Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"
Output: [2,1,1,1,1,1,1]
Explanation: Node 0 has label 'a' and its sub-tree has node 2 with label 'a' as well, thus the answer is 2. Notice that any node is part of its sub-tree.
Node 1 has a label 'b'. The sub-tree of node 1 contains nodes 1,4 and 5, as nodes 4 and 5 have different labels than node 1, the answer is just 1 (the node itself).
Example 2:


Input: n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb"
Output: [4,2,1,1]
Explanation: The sub-tree of node 2 contains only node 2, so the answer is 1.
The sub-tree of node 3 contains only node 3, so the answer is 1.
The sub-tree of node 1 contains nodes 1 and 2, both have label 'b', thus the answer is 2.
The sub-tree of node 0 contains nodes 0, 1, 2 and 3, all with label 'b', thus the answer is 4.
'''


class Solution:
    def countSubTrees(self, n: int, edges, labels: str):
        adj = {i: [] for i in range(n)}

        for u, v in edges:
            adj[u].append([v, labels[v]])
            adj[v].append([u, labels[u]])
            # update the char

        res = [0] * n

        def dfs(node, parent, char):
            print({
                'node': node,
                'parent': parent,
                'char': char,
            })
            res[node] = 1 if char == labels[node] else 0
            for child, c in adj[node]:
                if child == parent:
                    continue
                dfs(child, node, c)
                res[node] += res[child] if c == char else 0

        dfs(0, -1, labels[0])
        return res

    def solution2(self, n, edges, labels):
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        res = [0] * n

        def helper(node, parent):
            current_count = [0]*26
            for child in adj[node]:
                if child != parent:
                    c = helper(child, node)
                    for i in range(26):
                        current_count[i] += c[i]

            current_count[ord(labels[node])-ord('a')] += 1

            res[node] = current_count[ord(labels[node])-ord('a')]
            return current_count

        helper(0, -1)

        return res

if __name__ == "__main__":
    n = 7
    edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
    labels = "abaedcd"
    print(Solution().solution2(n, edges, labels))
