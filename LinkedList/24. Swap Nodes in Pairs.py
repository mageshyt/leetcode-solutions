# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = nex


class Solution:

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head) # act of dummy node

        prev=dummy
        current=head

        while current:
            first =current
            second=current.next

            # out of bounce case
            if not second:
                break

            # swap process

            # second should come first  [1,2,3,4] here 2-> ......
            prev.next=second

            # now first should map to second next 1->3.....

            first.next=second.next

            # second next should be first 2->1->3....

            second.next=first


            # re initialize

            prev=first 
            current=first.next # it will move to 3->4...

        return dummy.next

