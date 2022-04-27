import heapq
from operator import ne


class Solution:
    def minCostConnectPoints(self, points) :
        length=len(points)
        adj={i:[] for i in range(length)}
        for i in range(length):
            x1,y1=points[i]
            for j in range(i+1,length):
                x2,y2=points[j]
                dist=abs(x1-x2)+abs(y1-y2) # distance to connect
                adj[i].append((dist,j))
                adj[j].append((dist,i))
        
        # we are going to apply prims algo
        min_cost=0
        visited=set()
        #min heap going t have [cost,dist]
        heap=[[0,0]]
        while len(visited) < length:
            cost,node=heapq.heappop(heap)
            if node in visited: # if we have already visited this node then ignore
                continue
            
            min_cost+=cost
            visited.add(node) # add to visited
            for cost,nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(heap,[cost,nei])
        return min_cost

test=Solution()
points= [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(test.minCostConnectPoints(points))
        