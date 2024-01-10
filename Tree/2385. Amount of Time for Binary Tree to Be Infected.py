from collections import deque,defaultdict

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph=self.buildGraph(root)
        time=0

        queue=deque([start])

        visited=set()

        while queue:
            for _ in range(len(queue)):
                node=queue.popleft()
                visited.add(node)

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

            time+=1

        return time-1
    
    def buildGraph(self,root):
        graph=defaultdict(list)

        queue=deque([root])

        while queue:
            node=queue.popleft()

            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                # add the node to the queue
                queue.append(node.left)

            if node.right:

                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                # add the node to the queue
                queue.append(node.right)

        return graph
        


