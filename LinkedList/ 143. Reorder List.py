class Solution:
    # Time: O(N) | Space: O(1)
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        slow=fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        # reverse the second half
        prev=None
        curr=slow

        while curr:
            temp_next=curr.next
            curr.next=prev
            prev=curr
            curr=temp_next

        # merge the two halves
            
        first=head
        second=prev

        while second.next:
            temp_first=first.next
            temp_second=second.next

            first.next=second
            second.next=temp_first

            first=temp_first
            second=temp_second
        return head
    
    # Time: O(N) | Space: O(N)

    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes=[]

        while head:
            nodes.append(head)
            head=head.next

        left=0
        right=len(nodes)-1

        while left<right:
            nodes[left].next=nodes[right]
            left+=1

            if left==right:
                break

            nodes[right].next=nodes[left]
            right-=1

        nodes[left].next=None

        return nodes[0]
    
    