class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        results = defaultdict(list) 
        
        queue = [ (root, 0, 0) ] # store node, x, y
        
        while queue:
            node, pos, depth = queue.pop(0) # pop the first element
            if not node: continue # if node is None, continue
            results[(pos,depth)].append(node.val) # store the node value
            results[(pos,depth)].sort() # sort the list
            queue.extend( [ (node.left, pos-1, depth+1), (node.right, pos+1, depth+1) ] )
            
            
        res = defaultdict(list) # store the result
        keys = sorted(list(results.keys()), key=lambda x: (x[0], x[1]))
        
        
        for k in keys:
            pos, depth = k # get the position and depth
            res[pos].extend(results[k])

        return res.values()