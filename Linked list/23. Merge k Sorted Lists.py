'''You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []'''

import heapq


class Solution:
    def mergeKLists(self, lists):
        # use heap

        heap = []

        for i in range(len(lists)):
            # if the list is empty, skip
            if not lists[i]:
                continue
                # add the start node value and i and node itself
            heapq.heappush(heap, (lists[i].val, i, lists[i]))

        # create a dummy node
        dummy = ListNode(0)

        # create a pointer
        pointer = dummy
        while heap:
            # pop the smallest value from heap
            val, idx, node = heapq.heappop(heap)
            dummy.next = node
            dummy = dummy.next

            # if the node has next node, add it to heap
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))

        return pointer.next

        # [(1, 0, ListNode{val: 1, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}),
        # (1, 1, ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}),
        #  (2, 2, ListNode{val: 2, next: ListNode{val: 6, next: None}})]
