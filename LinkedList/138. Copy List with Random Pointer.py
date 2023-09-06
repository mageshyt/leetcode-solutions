"""

A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # Create a dictionary to store the mapping between original nodes and their corresponding new nodes
        hash_map = {}

        def dfs(node):
            if not node:
                return None

            # If the current node has already been processed, return its corresponding new node from the dictionary
            if node in hash_map:
                return hash_map[node]

            # Create a new node with the same value as the original node
            new_node = Node(node.val)
            
            # Store the mapping between the original node and the new node in the dictionary
            hash_map[node] = new_node

            # Recursively copy the 'next' pointer of the original node and connect it to the new node
            new_node.next = dfs(node.next)

            # Recursively copy the 'random' pointer of the original node and connect it to the new node
            new_node.random = dfs(node.random)

            # Return the new node
            return new_node

        # Start the deep copy process from the 'head' of the original linked list
        return dfs(head)

    

