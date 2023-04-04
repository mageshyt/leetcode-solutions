"""Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []"""
import collections


class Solution:
    def zigzagLevelOrder(self, root):

        if not root:
            return []

        queue = collections.deque()
        queue.append(root)  # add root to queue
        result = []

        while queue:
            level = []  # level list
            for _ in range(len(queue)):
                node = queue.popleft()  # pop left
                level.append(node.val)  # add to level list
                if node.left:
                    queue.append(node.left)  # if left child add to queue
                if node.right:
                    queue.append(node.right)  # if right child add to queue

            result.append(level)  # add level list to result

        for i in range(len(result)):
            if i % 2 == 1:  # if odd index then reverse
                result[i].reverse()

        return result
