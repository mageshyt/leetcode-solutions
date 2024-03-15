"""
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.



(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Example 3:

Input: head = [1,2,3,-3,-2]
Output: [1]

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        prefix_sum_to_node = {0: dummy}
        node = head

        while node:
            # calculate prefix sum
            prefix_sum += node.val
            # check if prefix sum already exists in the map
            if prefix_sum in prefix_sum_to_node:
                # if yes, remove all nodes between the prefix sum and the current node
                to_delete = prefix_sum_to_node[prefix_sum].next
                temp_sum = prefix_sum + to_delete.val
                while to_delete != node:
                    # remove the prefix sum to node mapping
                    del prefix_sum_to_node[temp_sum]
                    # move the pointer
                    to_delete = to_delete.next
                    temp_sum += to_delete.val
                prefix_sum_to_node[prefix_sum].next = node.next

            else:
                # if no, add the prefix sum to the map
                prefix_sum_to_node[prefix_sum] = node
            # move the pointer
            node = node.next

        return dummy.next
