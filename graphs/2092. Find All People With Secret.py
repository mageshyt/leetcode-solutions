from collections import defaultdict


class Solution:
    # Time: O(nlogn) | Space: O(n)
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        secrets=set([0,firstPerson]) # people with secrete

        # basesd on time
        time_map={} # time:meetings
        for src,dist , t in meetings:
            if t not in time_map:
                time_map[t]=defaultdict(list)
            time_map[t][src].append(dist)
            time_map[t][dist].append(src)

        def dfs(src,adj):
            if src in visted:
                return
            visted.add(src)
            secrets.add(src)

            for nei in adj[src]:
                if nei not in visted:
                    dfs(nei,adj)



        for t in sorted(time_map.keys()):
            visted=set()
            # consider as source node
            for src in time_map[t]:

                if src in secrets:
                    dfs(src,time_map[t])

        # print(time_map)
        return list(secrets)
