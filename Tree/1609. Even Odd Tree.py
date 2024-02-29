class Solution:
    # Time : O(n) | Space : O(n)
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue=deque([root])

        level=0

        while queue:
            prev=None
            for _ in range(len(queue)):
                node=queue.popleft()
                # if even level the we need to have odd values in decreasing order
                if level%2==0:
                    if node.val % 2 ==0 or (prev and prev >= node.val):
                        return False
                    
                # if odd level the we need to have even values in increasing order
                else:
                    if node.val % 2 !=0 or (prev and prev <= node.val):
                        return False
                # update the prev value
                prev=node.val

                if node.left:

                    queue.append(node.left)
                if node.right:

                    queue.append(node.right)

            level+=1

        return True

