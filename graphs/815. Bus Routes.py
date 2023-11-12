from collections import defaultdict, deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        # 1. Build a graph

        graph = defaultdict(list)

        for i, route in enumerate(routes):
            for stop in route:
                graph[stop].append(i)

        # 2. Find the start point

        start = graph[source]
        end = graph[target]

        # 3. Traverse the graph

        visited = set()
        queue = deque() # get the all the buses that can reach the start point

        for bus in start:
            # add the bus and the level
            queue.append((bus, 1))
            visited.add(bus) 

        while queue:
            # get the bus and the level
            bus, level = queue.popleft()

            if bus in end:
                return level

            for stop in routes[bus]:
                for neighbor in graph[stop]:
                    if neighbor not in visited:
                        queue.append((neighbor, level + 1))
                        visited.add(neighbor)

        return -1
    