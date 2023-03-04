"""Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false"""



class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if not head:
            return True

        # find the middle of the linked list
        slow = fast = head
        rev= None
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            # because the fast pointer is moving twice as fast as the slow pointer  
            # if the fast pointer reaches the end of the list, the slow pointer will be in the middle
            slow = slow.next

        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next

        return not rev
    

class Solution:
    def oddEvenList(self, head):

        if head is None:
            return None

        odd = head
        even = head.next  # even starts from 2nd node
        evenHead = even

        while even and even.next:
            odd.next = even.next  # always even.next will be odd

            odd = odd.next  # move odd to next odd node

            even.next = odd.next  # always odd.next will be even
            even = even.next  # move even to next even node

        odd.next = evenHead  # connect odd to even head

        return hea
