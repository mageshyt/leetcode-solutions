class Solution:
    def partition(self, head , x: int) :

        # logic
        # [left] will contain all the val less than x
        # [right] will contain wll the value grater | equal to x

        # finally we will join them


        left=ListNode(0)

        right=ListNode(0)
        
        leftTail=left
        rightTail=right
        while head:
            if head.val <x:
                leftTail.next=ListNode(head.val)
                leftTail=leftTail.next

            else:
                rightTail.next=ListNode(head.val)
                rightTail=rightTail.next


            head=head.next

        leftTail.next=right.next
        rightTail.next=None

        return left.next