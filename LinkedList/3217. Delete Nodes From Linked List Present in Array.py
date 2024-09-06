


from typing import List, Optional
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        ans=ListNode(0)

        nums=set(nums)

        ans.next=head

        prev=ans

        while head:
            if head.val in nums:
                prev.next=head.next
            else:
                prev=head
            head=head.next

        return ans.next

# Time complexity: O(N)
# Space complexity: O(N)
