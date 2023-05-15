'''Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000'''


class Solution:
    def reverseList(self, head):
        rev = None

        temp = head

        while temp:
            next_node = temp.next

            temp.next = rev

            rev = temp

            temp = next_node

        return rev
