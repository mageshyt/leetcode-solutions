from typing import  List

from collections import deque

class Solution:
    def largestValues(self, root) -> List[int]:

        res=[]

        if not root:
            return res
        
        queue=deque()

        queue.append(root)

        while queue:
            size=len(queue)

            curr_max=float('-inf')

            for _ in range(size):

                curr=queue.popleft()

                curr_max=max(curr_max,curr.val)
                # if its left child exists, append it to queue
                if curr.left:
                    queue.append(curr.left)

                # if its right child exists, append it to queue
                if curr.right:
                    queue.append(curr.right)

            res.append(curr_max)
        return res
    


# Time complexity: O(n)
# Space complexity: O(n) for queue

            

       