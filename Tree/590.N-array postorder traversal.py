"""
# Definition for a Node.
"""

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

from typing import List
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # base case
        if not root:
            return []

        res = []

        for child in root.children:
            res.extend(self.postorder(child))

        res.append(root.val)

        return res



