import collections


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        color = [0]*len(graph)

        queue = collections.deque()

        for i in range(len(graph)):
            # if not visited then mark it as 1 (blue)
            if color[i] == 0:
                queue.append(i)
                color[i] = 1

                # now make all the neighbors as -1 (red)
                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if color[neighbor] == 0:
                            color[neighbor] = -color[node]
                            queue.append(neighbor)
                        elif color[neighbor] == color[node]:
                            # which means it is not bipartite
                            return False

        return True
    
    def isBipartite(self, graph: List[List[int]]) -> bool:

        # dfs solution

        color = [0]*len(graph)

        def dfs(node,c):
            color[node]=c
            for neighbor in graph[node]:
                if color[neighbor]==c:
                    return False
                if color[neighbor]==0 and not dfs(neighbor,-c):
                    return False
                
            return True
        

        for i in range(len(graph)):
            if color[i]==0 and not dfs(i,1):
                return False
            
        return True


        


