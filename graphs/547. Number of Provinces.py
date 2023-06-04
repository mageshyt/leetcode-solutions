class Solution:
    def findCircleNum(self, isConnected) -> int:
        res=0

        def dfs(start):
            # mark as visited
            visited.add(start)

            # visit all neighbors

            for i in range(len(isConnected)):
                # if not visited and connected
                if i not in visited and isConnected[start][i]==1:
                    dfs(i)


                


        visited=set()

        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                res+=1

        return res
            
