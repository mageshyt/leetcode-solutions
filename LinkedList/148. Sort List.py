

"""Given the head of a linked list, return the list after sorting it in ascending order.

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]"""


class Solution:
    def sortList(self, head):
        # base case
        if not head or head.next:
            return head

        fast, slow = head.next, head  # slow will give us the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next  # first half
        slow.next = None

        l = self.sortList(head)
        r = self.sortList(second)

        return self.merge(l, r)

    def merge(self, left, right):
        if left is None:
            return right
        elif right is None:
            return left

        dummy = ListNode(0)  # dummy pointer
        head = dummy

        while left and right:
            # if left is < than right we need

            if left.val <= right.val:
                head.next = left
                # move left pointer
                left = left.next

            else:
                head.next = right
                right = right.next

            # now p pinter

            head = head.next

        # join the remaining node only one node will be remaining

        head.next = left if right is None else right

        return dummy.next
