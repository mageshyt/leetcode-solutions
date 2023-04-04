
    def longestCycle(self, edges) -> int:

        def dfs(node):
            if node not in seen:

                if node in vis:
                    self.mxl = max(self.mxl, len(vis) - vis[node])

                elif edges[node] != -1:

                    vis[node] = len(vis)
                    dfs(edges[node])
                    vis.pop(node)

                seen[node] = True

        self.mxl = -1
        seen = {}
        vis = {}

        for i in range(len(edges)):
            dfs(i)

        return self.mxl

