
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        # [key:bomb] -> [value:adjacent bombs]
        adj = collection.defaultdict(list)

        for i in range(len(bombs)):
            for j in range(i+1, len(bombs)):
                x1, y1, r1 = bombs[i]  # bomb1 x-coord, y-coord, radius
                x2, y2, r2 = bombs[j]  # bomb2 x-coord, y-coord, radius

                # now find the distance between the two bombs
                # distance between two bombs
                dist = sqrt((x1-x2)**2+(y1-y2)**2)

                # if the distance is less than or equal to the radius of the bomb, then the two bombs are adjacent
                if dist <= r1:
                    adj[i].append(j)

                if dist <= r2:
                    adj[j].append(i)

        # now we have the adjacency list, we can use dfs to find the maximum number of bombs that can be detonated
        def dfs(node, visited):
            if node in visited:
                return 0
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)

            # return the number of bombs that can be detonated
            return len(visited)
        res = 0
        for i in range(len(bombs)):

            res = max(res, dfs(i, set()))

        return res
