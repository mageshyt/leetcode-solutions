'''Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
'''


from collections import deque


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        queue = deque()

        queue.append(root)

        result = []

        while queue:
            level = []

            for _ in range(len(queue)):
                pop = queue.popleft()
                level.append(pop.val)
                if pop.left:
                    queue.append(pop.left)
                if pop.right:
                    queue.append(pop.right)

            result.append(level)

        return result
