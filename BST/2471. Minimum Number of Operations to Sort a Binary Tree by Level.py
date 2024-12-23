"""
You are given the root of a binary tree with unique values.

In one operation, you can choose any two nodes at the same level and swap their values.

Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.

The level of a node is the number of edges along the path between it and the root node.

 Example 1:


Input: root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
Output: 3
Explanation:
- Swap 4 and 3. The 2nd level becomes [3,4].
- Swap 7 and 5. The 3rd level becomes [5,6,8,7].
- Swap 8 and 7. The 3rd level becomes [5,6,7,8].
We used 3 operations so return 3.
It can be proven that 3 is the minimum number of operations needed.
"""

from typing import Optional
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q=deque([(root,0)]) # node and level

        result=0

        def helper(level):
            pos={val:idx for idx,val in enumerate(sorted(level))}

            visited=set()

            swaps=0

            for i in range(len(level)):
                cnt=0

                while not i in visited and i != pos[level[i]]:
                    visited.add(i)
                    i=pos[level[i]]
                    cnt+=1

                swaps+=max(0,cnt-1)
            return swaps

               

        while q:
            values=[]
            for _ in range(len(q)):
                node, level=q.popleft()
                values.append(node.val)

                if node.left:
                    q.append((node.left,level+1))

                if node.right:
                    q.append((node.right,level+1))
            
            result+=helper(values)

        return result





root=TreeNode(1)
root.left=TreeNode(4)
root.right=TreeNode(3)
root.left.left=TreeNode(7)
root.left.right=TreeNode(6)
root.right.left=TreeNode(8)
root.right.right=TreeNode(5)
root.left.left.right=TreeNode(9)
root.right.left.right=TreeNode(10)

print(Solution().minimumOperations(root)) # 3
