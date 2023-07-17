"""You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        # Reverse both lists
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        
        # Add the reversed lists
        result = self.add(l1, l2)
        
        # Reverse the result
        return self.reverse(result)
    
    def reverse(self, head):
        prev = None
        curr = head
        
        # Reverse the list by manipulating the next pointers
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Return the new head of the reversed list
        return prev
    
    def add(self, l1, l2):
        carry = 0
        result = None

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and carry
            _sum = val1 + val2 + carry
            carry = _sum // 10
            _sum = _sum % 10

            if not result:
                result = ListNode(_sum)
                temp = result
            else:
                temp.next = ListNode(_sum)
                temp = temp.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        # If there's still a carry, add it as a new node
        if carry:
            temp.next = ListNode(carry)

        # Return the head of the result list
        return result

# Compare this snippet from LinkedList/234. Palindrome Linked List.py:





 