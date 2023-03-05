"""Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You do not need to jump.
Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array."""

import collections


class Solution:
    def minJumps(self, arr) -> int:

        # bfs
        # time: O(n)
        # space: O(n)
        # 1. build graph
        # 2. bfs
        # 3. return steps
        # 4. if not found, return -1

        # 1. build graph
        graph = collections.defaultdict(list)
        for i, v in enumerate(arr):
            graph[v].append(i)

        # 2. bfs
        q = collections.deque([(0, 0)])
        visited = set()
        while q:
            node, steps = q.popleft()
            if node == len(arr) - 1:
                return steps
            visited.add(node)
            # all the same value nodes and the previous and next node
            for nei in graph[arr[node]] + [node - 1, node + 1]:
                if 0 <= nei < len(arr) and nei not in visited:
                    q.append((nei, steps + 1))
            graph[arr[node]] = []

            print(q, visited)
        return -1


# Path: bfs and dfs/1346. Check If N and Its Double Exist.py
if __name__ == "__main__":
    s = Solution()
    print(s.minJumps([100, -23, -23, 404, 100, 23, 23, 23, 3, 404]))
