
'''You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)

        prev = dummy

        while list1 and list2:
            val_1 = list1.val
            val_2 = list2.val

            # if val_1 is greater than val 2

            if val_1 > val_2:
                # we move pointer to next value in list 2
                prev.next = list2
                list2 = list2.next

            else:
                prev.next = list1
                list1 = list1.next

            prev = prev.next

        if list1:
            prev.next = list1

        else:
            prev.next = list2

        return dummy.next

    def mergeTwoLists(self, list1, list2):
        # if list1 is empty or list 2
        if not list1 or not list2:
            return list1 or list2

        # if list1 is greater than list2

        if list1.val > list2.val:
            # we have to move the list2 to next value
            list2.next = self.mergeTwoLists(list1, list2.next)

            return list2

        else:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
