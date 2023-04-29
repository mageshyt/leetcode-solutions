from math import comb


class Solution:
    def numberOfGoodPaths(self, vals, edges) -> int:

        UF = {}
        def find(x):
            UF.setdefault(x,x) # default set
            if x != UF[x]:
                UF[x] = find(UF[x]) 
            return UF[x]

        # to find union
        def union(x,y):
            UF[find(x)] = find(y)
        
        tree = defaultdict(list)
        # Using a hashmap of set to get the nodes with the same value
        val2Nodes = defaultdict(set)
        for s,e in edges:
            # add the edge to the tree
            tree[s].append(e)
            tree[e].append(s)
            # add the node to the hashmap of set
            val2Nodes[vals[s]].add(s)
            val2Nodes[vals[e]].add(e)
        
        res = len(vals) # every node is a path so add len(vals) to the result
        
        # Sort the value, and start to union the nodes with the current v that we are checking and their neighbors (have smaller values than the current v).
        for v in sorted(val2Nodes.keys()):
            for node in val2Nodes[v]:
                for nei in tree[node]:
                    if vals[nei] <= v:
                        union(node,nei)
            
            # For each group, we need to count the number of elements with value==v in this group.
            groupCount = defaultdict(int)
            for node in val2Nodes[v]:
                groupCount[find(node)] += 1
                
            for root in groupCount.keys():
                # if there are n number of nodes that have value==v in the a group. 
                
                res += comb(groupCount[root],2)
        
        return res



if __name__ == "__main__":
    s=Solution()
    print(s.numberOfGoodPaths([1,2,3,4,5,6,7,8,9,10],[[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9]]))